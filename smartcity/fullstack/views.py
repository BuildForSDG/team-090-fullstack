from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import ServiceProvider, CustomerProfile, Subscription
from .forms import (ServiceProviderProfileForm,
                    CustomerProfileForm)
from .forms import CustomerRegistration
from django.contrib.auth import authenticate, logout, login

# Create your views here.


def home(request):
    context = {}
    return render(request, 'fullstack/home.html', context)


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


def service_provider_profile(request, service_provider_id):
    """View function for the service provider's profile page."""
    template_name = 'fullstack/service_profile.html'
    service_provider = get_object_or_404(ServiceProvider,
                                         pk=service_provider_id)
    context = {'service_provider': service_provider}
    return render(request, template_name, context)


def customer_profile(request):
    """View function for the customer's profile page."""
    template_name = 'fullstack/customer_profile.html'
    # user_profile = CustomerProfile.objects.get(user.id=request.user.id)
    user_profile = get_object_or_404(CustomerProfile, user_id=request.user.id)
    try:
        services = get_object_or_404(Subscription,
                                     customer_id=user_profile.user.id)
    except Subscription.DoesNotExist:
        services = None
    context = {'user_profile': user_profile, 'services': services}
    return render(request, template_name, context)


def create_customer_profile(request):
    template_name = 'fullstack/customer_profile.html'
    context = None
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            context = {'user_profile': user_profile}
            return render(request, template_name, context)
    else:
        form = CustomerProfileForm()
        context = {'form': form}
        template_name = 'fullstack/customer_profile_form.html'
        return render(request, template_name, context)
    return HttpResponseRedirect(reverse('fullstack:create_customer_p'))


def create_service_provider_profile(request):
    """Create returns empty registration form or save filled form"""
    template_name = 'fullstack/provider_profile.html'
    if request.method == 'POST':
        form = ServiceProviderProfileForm(request.POST, request.FILES)
        if form.is_valid():
            provider_profile = form.save(commit=False)
            provider_profile.user = request.user
            provider_profile.save()
            context = {'service_provider': provider_profile}
            return render(request, template_name, context)
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
