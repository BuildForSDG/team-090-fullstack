"""Urls of the fullstack app are contained here"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('', views.login),
    path('', views.service_provider_profile),
    path('', views.customer_profile),
    path('', views.sign_up),
    path('', views.categories),
]
