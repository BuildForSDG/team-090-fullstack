"""Urls of the fullstack app are contained here."""

from django.urls import path
from . import views
from smartcity import settings
from django.conf.urls.static import static

app_name = 'fullstack'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('providerprofile/<int:service_provided_id>/',
         views.service_provider_profile, name='provider_profile'),
    path('customerprofile/', views.customer_profile, name='customer_profile'),
    path('signup/', views.sign_up, name='signup'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('profilechoice/', views.profile_choice, name='choice'),
    path('createproviderprofile/', views.create_service_provider_profile,
         name='create_provider_p'),
    path('createcustomerprofile/', views.create_customer_profile,
         name='create_customer_p'),
    path('editprofile/<int:user_id>/', views.edit_profile,
         name='edit_profile'),
    path('reviewandrating/<int:service_id>/', views.reviews_and_ratings,
         name='rating'),
    path('registration/', views.customer_registration, name='registration'),
    path('editproviderprofile/<int:service_provided_id>/',
         views.edit_service_provider_profile, name='edit_provider_profile'),
    path('servicedetails/<int:service_id>/', views.service_details,
         name='service_details'),
    path('subscribe/<int:service_id>/', views.subscribe, name='subscribe'),
    path('ajax/states/', views.get_states, name='get_states'),
    path('ajax/cities/', views.get_cities, name='get_cities'),
    path('ajax/states/name/', views.get_states_by_name, name='get_states_by_name'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
