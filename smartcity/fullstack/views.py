from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import (ServiceProvider, CustomerProfile,
                     Subscription, Suspension)
from .forms import (ServiceProviderProfileForm,
                    CustomerProfileForm)
from .forms import CustomerRegistration
from django.contrib.auth import authenticate, logout, login
from cities_light.models import City, Region, Country

# Create your views here.


def home(request):
    """ Returns context with coutries, regions and cities."""
    template_name = 'fullstack/home.html'
    country = Country.objects.all() 
    region = Region.objects.all()
    city = City.objects.all()
    context = {'countries': country, 'regions': region, 'cities': city}
    return render(request, template_name, context)


def index(request):
    """View function for the index page."""
    return render(request, 'base.html', {})


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
    try:
        subscription = Subscription.objects.filter(
            service_provider_id=service_provided_id)
        suspension = Suspension.objects.get(
            service_provider_id=service_provided_id)
    except Subscription.DoesNotExist:
        subscription = None
    except Suspension.DoesNotExist:
        suspension = None
    user_profile = CustomerProfile.objects.get(user_id=request.user.id)
    service_provided = ServiceProvider.objects.get(
                            id=service_provided_id)
    context = {'service_provided': service_provided,
               'user_profile': user_profile, 'suspension': suspension,
               'subscription': subscription}
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
    except CustomerProfile.DoesNotExist:
        user_profile = None
        services_provided = None
    except ServiceProvider.DoesNotExist:
        services_provided = None
    else:
        try:
            services_subscribed = Subscription.objects.filter(
                                     customer_id=user_profile.user.id)
        except Subscription.DoesNotExist:
            services_subscribed = None
    context = {'user_profile': user_profile, 'services': services_subscribed,
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


def reviews_and_ratings(request, provider_id):
    """View function for the customers review and ratings page."""
    return render(request, '.html', {})


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
    messages.info(request, "Successfully logged out!")
    return redirect('fullstack:home')


def search(request):
    pass
