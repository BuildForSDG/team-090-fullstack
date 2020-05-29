from django.forms import ModelForm
# from cities_light.models import Country, Region, City
from .models import ServiceProvicer, CustomerProfile


class ServiceProviderProfileForm(ModelForm):
    class Meta:
        """Generate fields from ServiceProvider model"""
        model = ServiceProvicer
        exclude = ['rating', 'user']


class CustomerProfileForm(ModelForm):
    class Meta:
        """Generate fields from CustomerProfile model"""
        model = CustomerProfile
        exclude = ['user']
