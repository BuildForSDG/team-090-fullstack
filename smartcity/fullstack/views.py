from django.shortcuts import render

# Create your views here.


def index(request):
    """View function for the index page."""
    return render(request, 'base.html', {})


def login(request):
    """View function for the login page."""
    return render(request, '.html', {})


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
