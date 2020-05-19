from django.db import models
from django.utils import timezone
from cities_light.models import City, Region, Country

# Create your models here.


class Category(models.Model):
    """ Model for service categories"""
    name = models.CharField(max_length=100)
    document_required = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    """ Model for services rendered"""
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.Foreignkey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class ServiceProvider(models.Model):
    """Model for service providers"""
    business_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service_rendered = models.CharField(max_length=50)
    service_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/')
    description = models.TextField(max_length=200)
    years_of_experience = models.IntegerField()
    year_of_establishement = models.DateField(default=timezone.now)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    supporting_document = models.FileField(upload_to='uploads/', null=True)
    rating = models.FloatField()

    def __str__(self):
        return f'{self.business_name}'