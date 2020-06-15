from django.contrib import admin
from .models import (Service, Category, Suspension,
                     Subscription, ServiceProvider,
                     CustomerProfile, RatingAndReview)
# from cities_light.models import City, Region, Country

# Register your models here.

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(ServiceProvider)
admin.site.register(CustomerProfile)
admin.site.register(Subscription)
admin.site.register(Suspension)
admin.site.register(RatingAndReview)
