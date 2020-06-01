from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ServiceProvider, CustomerProfile
from .forms import (ServiceProviderProfileForm,
                    CustomerProfileForm)

# Create your views here.


def home(request):
    context = {}
    return render(request, 'fullstack/home.html', context)


def index(request):
    """View function for the index page."""
    return render(request, 'base.html', {})


def login(request):
    """View function for the login page."""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('fullstack:home'))
    else:
        context = {}
    return render(request, 'fullstack/login.html', context)


def logout(request):
    pass


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
    context = {'user_profile': user_profile}
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
    template_name = 'fullstack/provider_profile.html'
    if request.method == 'POST':
        form = ServiceProviderProfileForm(request.POST, request.FILES)
        if form.is_valid():
            provider_profile = form.save(commit=False)
            provider_profile.user = request.user
            provider_profile.rating = 0
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


def search(request):
    pass
