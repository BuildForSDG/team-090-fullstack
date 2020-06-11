from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import (ServiceProvider, CustomerProfile,
                     Subscription, Suspension, Service,
                     Category, RatingAndReview)
from .forms import (ServiceProviderProfileForm,
                    CustomerProfileForm, RatingAndReviewForm)
from .forms import CustomerRegistration
from django.contrib.auth import authenticate, logout, login
from cities_light.models import City, Region, Country
from django.utils import timezone

# Create your views here.


def get_subscribed_services(user_id):
    services_subscribed = None
    try:
        customer_profile = CustomerProfile.objects.get(user_id=user_id)
        services_subscribed = Subscription.objects.filter(
            customer_id=customer_profile.id)
    except CustomerProfile.DoesNotExist:
        return None
    except Subscription.DoesNotExist:
        return None
    return services_subscribed


def get_country_region_city_ids_from_user(user_id):
    """Returns country, region and city ids from user profile."""
    results = None
    try:
        user_profile = CustomerProfile.objects.get(user_id=user_id)
        results = [user_profile.country_id,
                   user_profile.region_id,
                   user_profile.city_id]
    except CustomerProfile.DoesNotExist:
        results = None
    return results


def get_service_from_location(keyword, country_id, region_id, city_id):
    """Returns services based on keyword,user's country,region and city."""
    results = None
    try:
        results = ServiceProvider.objects.filter(
            business_name__icontains=keyword,
            country_id=country_id,
            region_id=region_id,
            city_id=city_id)
        if not results:
            results = ServiceProvider.objects.filter(
                description__icontains=keyword,
                country_id=country_id,
                region_id=region_id,
                city_id=city_id)
    except CustomerProfile.DoesNotExist:
        results = None
    return results


def get_services_and_categories():
    try:
        categories = Category.objects.all()
        services = Service.objects.all()
    except Category.DoesNotExist:
        categories = None
    except Service.DoesNotExist:
        services = None
    return categories, services


def home(request):
    """Returns context with coutries, regions and cities."""
    template_name = 'fullstack/home.html'
    services = None
    categories = None
    customer_profile = None
    if request.user.is_authenticated:
        try:
            customer_profile = CustomerProfile.objects.get(
              user_id=request.user.id)
        except CustomerProfile.DoesNotExist:
            customer_profile = None
    country = Country.objects.all()
    region = Region.objects.all()
    city = City.objects.all()
    categories, services = get_services_and_categories()
    context = {'countries': country, 'regions': region,
               'cities': city, 'services_list': services,
               'categories': categories,
               'customer_profile': customer_profile}
    return render(request, template_name, context)


def index(request):
    """View function for the index page."""
    return render(request, 'fullstack/landing.html', {})


def user_login(request):
    """Authenticate user login credentials."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('fullstack:home'))
        messages.error(request, 'Either username or password is wrong!')
        return redirect('fullstack:login')
    template_name = 'fullstack/login.html'
    return render(request, template_name, {})


def edit_profile(request, user_id):
    template_name = 'fullstack/provider_profile_form.html'
    context = {}
    return render(request, template_name, context)


def profile_choice(request):
    template_name = 'fullstack/profile_choice.html'
    context = {}
    return render(request, template_name, context)


def service_provider_profile(request, service_provided_id):
    """View function for the service provider's profile page."""
    template_name = 'fullstack/provider_profile.html'
    suspension = None
    subscription = None
    ratings_and_reviews = None
    try:
        subscription = Subscription.objects.filter(
            service_provider_id=service_provided_id)
        suspension = Suspension.objects.get(
            service_provider_id=service_provided_id)
        ratings_and_reviews = RatingAndReview.objects.filter(
            service_provider_id=service_provided_id)
    except Subscription.DoesNotExist:
        subscription = None
    except Suspension.DoesNotExist:
        suspension = None
    except RatingAndReview.DoesNotExist:
        ratings_and_reviews = None
    user_profile = CustomerProfile.objects.get(user_id=request.user.id)
    service_provided = ServiceProvider.objects.get(
                            id=service_provided_id)
    context = {'service_provided': service_provided,
               'user_profile': user_profile, 'suspension': suspension,
               'subscriptions': subscription,
               'ratings': ratings_and_reviews}
    return render(request, template_name, context)


def customer_profile(request):
    """View function for the customer's profile page."""
    template_name = 'fullstack/customer_profile.html'
    # user_profile = CustomerProfile.objects.get(user.id=request.user.id)
    services_provided = None
    user_profile = None
    services_subscribed = None

    try:
        user_profile = CustomerProfile.objects.get(user_id=request.user.id)
        services_provided = ServiceProvider.objects.filter(
            user_id=request.user.id)
        services_subscribed = Subscription.objects.filter(
                                customer_id=user_profile.id)
    except CustomerProfile.DoesNotExist:
        user_profile = None
        services_provided = None
    except ServiceProvider.DoesNotExist:
        services_provided = None
    except Subscription.DoesNotExist:
        services_subscribed = None
    context = {'user_profile': user_profile,
               'services_subscribed': services_subscribed,
               'services_provided': services_provided}
    return render(request, template_name, context)


def create_customer_profile(request):
    """Returns empty or populated form for editing."""
    template_name = 'fullstack/customer_profile_form.html'
    user_profile = None
    try:
        user_profile = CustomerProfile.objects.get(user_id=request.user.id)
    except CustomerProfile.DoesNotExist:
        user_profile = None
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES)
        if user_profile:
            if 'picture' in request.FILES:
                user_profile.picture = request.FILES['picture']
            form = CustomerProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile_form = form.save(commit=False)
            user_profile_form.user = request.user
            user_profile_form.save()
            return redirect('fullstack:customer_profile')
    else:
        form = CustomerProfileForm(instance=user_profile)
        context = {'form': form}
        return render(request, template_name, context)
    return HttpResponseRedirect(reverse('fullstack:create_customer_p'))


def edit_service_provider_profile(request, service_provided_id):
    service_provided = ServiceProvider.objects.get(
                            id=service_provided_id)
    template_name = 'fullstack/provider_profile_form.html'
    if request.method == 'POST':
        if 'picture' in request.FILES:
            service_provided.picture = request.FILES['picture']
        if 'supporting_document' in request.FILES:
            service_provided.supporting_document = request.FILES[
                'supporting_document']
        form = ServiceProviderProfileForm(request.POST,
                                          instance=service_provided)
        if form.is_valid():
            form.save()
            return redirect('fullstack:provider_profile', service_provided_id)
    form = ServiceProviderProfileForm(instance=service_provided)
    context = {'form': form, 'service_provided_id': service_provided_id}
    return render(request, template_name, context)


def create_service_provider_profile(request):
    """Create returns empty registration form or save filled form."""
    template_name = 'fullstack/provider_profile.html'
    if request.method == 'POST':
        form = ServiceProviderProfileForm(request.POST, request.FILES)
        if form.is_valid():
            provider_profile = form.save(commit=False)
            provider_profile.user = request.user
            provider_profile.save()
            context = {'service_provider': provider_profile}
            return redirect('fullstack:customer_profile')
    else:
        form = ServiceProviderProfileForm()
        context = {'form': form}
        template_name = 'fullstack/provider_profile_form.html'
        return render(request, template_name, context)
    return HttpResponseRedirect(reverse('fullstack:create_provider_p'))


def sign_up(request):
    """View function for the sign up page."""
    return render(request, '.html', {})


def categories(request):
    """View function for the categories page."""
    return render(request, '.html', {})


def reviews_and_ratings(request, service_id):
    """View function for the customers review and ratings page."""
    template_name = 'fullstack/rating_error.html'
    rating = None
    review = None
    customer = None
    if request.method == 'POST':
        rating = request.POST['rating']
        review = request.POST['review']
        if request.user.is_authenticated:
            try:
                customer = CustomerProfile.objects.get(user_id=request.user.id)
                service_provider = ServiceProvider.objects.get(id=service_id)
                if not RatingAndReview.objects.filter(
                        customer_id=customer.id,
                        service_provider_id=service_provider.id).exists():
                    RatingAndReview.objects.create(
                        customer=customer, service_provider=service_provider,
                        rating=rating, review=review)
                else:
                    form = RatingAndReviewForm(
                        request.POST, instance=RatingAndReview.objects.get(
                            customer_id=customer.id,
                            service_provider_id=service_id))
                    form.save()
            except CustomerProfile.DoesNotExist:
                return render(request, template_name, {})
        else:
            return render(request, template_name, {})
    return redirect('fullstack:service_details', service_id=service_id)


def customer_registration(request):
    """Function for validating customer registration."""
    if request.method == "POST":
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            form.save()
            template_name = 'fullstack/success.html'
            return render(request, template_name, {})

    else:
        form = CustomerRegistration()
    return render(request, 'fullstack/registration.html', {'form': form})


def logout_user(request):
    logout(request)
    # messages.info(request, "Successfully logged out!")
    return redirect('fullstack:home')


def search(request):
    """Returns a service from search key-word."""
    results = None
    country_id = None
    region_id = None
    city_id = None
    services_subscribed = None
    keyword = None
    customer_profile = None
    template_name = 'fullstack/home.html'
    if request.method == 'POST':
        keyword = request.POST['keyword']
        if 'city' in request.POST:
            country_id = request.POST['country']
            region_id = request.POST['region']
            city_id = request.POST['city']
        elif request.user.is_authenticated:
            ids = get_country_region_city_ids_from_user(
                    request.user.id)
            if ids is not None:
                country_id, region_id, city_id = ids
            services_subscribed = get_subscribed_services(request.user.id)
            # get users profile
            try:
                customer_profile = CustomerProfile.objects.get(
                  user_id=request.user.id)
            except CustomerProfile.DoesNotExist:
                customer_profile = None
        if country_id and region_id and city_id:
            results = get_service_from_location(
                keyword, country_id, region_id, city_id)
    country = Country.objects.all()
    region = Region.objects.all()
    city = City.objects.all()
    categories_list, services_list = get_services_and_categories()
    context = {'services': results, 'countries': country,
               'regions': region, 'cities': city,
               'services_subscribed': services_subscribed,
               'services_list': services_list,
               'categories': categories_list,
               'keyword': keyword, 'customer_profile': customer_profile}
    return render(request, template_name, context)


def service_details(request, service_id):
    template_name = 'fullstack/service_details.html'
    rating_and_review = None
    customer_review = None
    form = RatingAndReviewForm()
    service_provided = get_object_or_404(
        ServiceProvider, pk=service_id)
    try:
        rating_and_review = RatingAndReview.objects.filter(
            service_provider_id=service_id)
    except RatingAndReview.DoesNotExist:
        rating_and_review = None
        # if user is login and has profile, get his submitted review
    if request.user.is_authenticated:
        try:
            customer = CustomerProfile.objects.get(user_id=request.user.id)
            customer_review = RatingAndReview.objects.get(
                customer_id=customer.id, service_provider_id=service_id)
            form = RatingAndReviewForm(instance=customer_review)
        except CustomerProfile.DoesNotExist:
            customer_review = None
        except RatingAndReview.DoesNotExist:
            customer_review = None
    context = {'service_provided': service_provided,
               'form': form, 'ratings': rating_and_review,
               'customer_review_and_rating': customer_review}
    return render(request, template_name, context)


def subscribe(request, service_id):
    """Subscribe a customer for a service."""
    customer = None
    if request.user.is_authenticated:
        try:
            customer = CustomerProfile.objects.get(user_id=request.user.id)
        except CustomerProfile.DoesNotExist:
            return render(request, 'fullstack/profile_error.html')
        try:
            Subscription.objects.get(customer_id=customer.id)
        except Subscription.DoesNotExist:
            Subscription.objects.create(
                customer_id=customer.id, service_provider_id=service_id,
                date=timezone.now())
        return redirect('fullstack:customer_profile')
    return render(request, 'fullstack/profile_error.html')
