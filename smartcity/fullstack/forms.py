from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from cities_light.models import Country, Region, City
from .models import ServiceProvider, CustomerProfile


class ServiceProviderProfileForm(ModelForm):
    class Meta:
        """Generate fields from ServiceProvider model"""
        model = ServiceProvider
        exclude = ['rating', 'user']


class CustomerProfileForm(ModelForm):
    class Meta:
        """Generate fields from CustomerProfile model"""
        model = CustomerProfile
        exclude = ['user']


class CustomerRegistration(UserCreationForm):
    """Customer registration"""
    username = forms.CharField(
        max_length=100, required=True, help_text="Enter User name"
    )
    email = forms.EmailField(
        max_length=250, required=True, help_text="Please enter your email"
    )
    password = forms.CharField(
        max_length=32, widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2'
        )

    def save_email(self, commit=True):
        user = super(CustomerRegistration, self).save(commit=False)
        User.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
