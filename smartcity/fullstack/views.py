from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .forms import CustomerRegistration
from django.contrib.auth import authenticate, logout

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


def customer_registration(request):
    """Function for validating customer registration."""
    if request.method == "POST":
        form = CustomerRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            # logs in user upon successful authentication.
            login(request, user)
            messages.success(
                request, f"Hello {username}, Welcome to Smart City"
            )
            return redirect('fullstack:login')
    else:
        form = CustomerRegistration()
        return render(request, 'registration.html', {'form': form})


def logout_customer(request):
    logout(request)
    messages.info(request, "Successfully logged out!")
    return redirect('fullstack:home')


def search(request):
    pass
