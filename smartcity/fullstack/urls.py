"""Urls of the fullstack app are contained here."""

from django.urls import path
from . import views

app_name = 'fullstack'
urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('providerprofile/', views.service_provider_profile, name='providerprofile'),
    path('customerprofile/', views.customer_profile, name='customerprofile'),
    path('signup/', views.sign_up, name='signup'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search')
]
