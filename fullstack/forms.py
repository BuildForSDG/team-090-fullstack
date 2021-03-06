from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from cities_light.models import Country, Region, City
from .models import (ServiceProvider,
                     CustomerProfile, RatingAndReview)


class ServiceProviderProfileForm(ModelForm):
    """Generate fields from ServiceProvider model."""
    class Meta:
        model = ServiceProvider
        exclude = ['approval', 'user']


class CustomerProfileForm(ModelForm):
    """Generate fields from CustomerProfile model."""
    class Meta:
        model = CustomerProfile
        exclude = ['user']


class CustomerRegistration(UserCreationForm):
    """Customer registration."""
    username = forms.CharField(
        max_length=100, required=True, help_text=""
    )

    first_name = forms.CharField(
        max_length=100, required=True, help_text=""
    )
    last_name = forms.CharField(
        max_length=100, required=True, help_text=""
    )
    email = forms.EmailField(
        max_length=250, required=True, help_text=""
    )

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2',)


class RatingAndReviewForm(ModelForm):
    """Generate review and rating form model."""
    class Meta:
        model = RatingAndReview
        fields = ['rating', 'review']
