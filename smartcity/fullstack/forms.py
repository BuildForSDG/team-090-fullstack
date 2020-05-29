from django.forms import ModelForm
# from cities_light.models import Country, Region, City
from .models import ServiceProvicer, CustomerProfile


class ServiceProviderProfileForm(ModelForm):
    class Meta:
        model = ServiceProvicer
        exclude = ['rating', 'user']


class CustomerProfileForm(ModelForm):
    class Meta:
        model = CustomerProfile
        exclude = ['user']
