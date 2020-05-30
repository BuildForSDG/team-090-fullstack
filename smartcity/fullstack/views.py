from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def service_provider_profile(request):
    """View function for the service provider's profile page."""
    return render(request, '.html', {})


def customer_profile(request):
    """View function for the customer's profile page."""
    return render(request, '.html', {})


def sign_up(request):
    """View function for the sign up page."""
    return render(request, '.html', {})


def categories(request):
    """View function for the categories page."""
    return render(request, '.html', {})


def reviews_and_ratings(request):
    """View function for the customers review and ratings page."""
    return render(request, '.html', {})


def search(request):
    pass
