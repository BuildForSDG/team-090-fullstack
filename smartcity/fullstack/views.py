from django.shortcuts import render

# Create your views here.

def index(request):
    """This is the view for the index page."""
    return render(request, '.html', {})


def login(request):
    """This is the view for the login page."""
    return render(request, '.html', {})


def service_provider_profile(request):
    """This is the view for the service provider's profile page."""
    return render(request, '.html', {})


def customer_profile(request):
    """This is the view for the customer's profile page."""
    return render(request, '.html', {})


def sign_up(request):
    """This is the view for the sign up page."""
    return render(request, '.html', {})


def categories(request):
    """This is the view for the categories page."""
    return render(request, '.html', {})


def reviews_and_ratings(request):
    """This is the view for the customers review and ratings page."""
    return render(request, '.html', {})
