from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cities_light.models import City, Region, Country
from phonenumber_field.modelfields import PhoneNumberField
from .my_currency import get_currencies_tuple


CURRENCY = get_currencies_tuple()
RATINGS = [
    ('Poor', 'Poor'),
    ('Good', 'Good'),
    ('Excellent', 'Excellent')
]
# Create your models here.


class Category(models.Model):

    """ Model for service categories."""
    name = models.CharField(max_length=100)
    document_required = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):

    """ Model for services rendered."""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Document(models.Model):

    """Model for document required from service provicer."""
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class ServiceProvider(models.Model):

    """Model for service providers."""
    business_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    service_rendered = models.ForeignKey(Service, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=100, choices=CURRENCY,
                                default=CURRENCY[98])
    picture = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=200)
    years_of_experience = models.IntegerField()
    year_of_establishement = models.DateField(default=timezone.now)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    supporting_document = models.FileField(upload_to='documents/', blank=True)
    document_type = models.ForeignKey(Document, on_delete=models.CASCADE,
                                      blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.business_name}'

    def document_required(self):
        if self.service_category.document_required:
            self.supporting_document.blank = False


class CustomerProfile(models.Model):
    """Model for customer's profile."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    street_address = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.user.first_name}'


class Subscription(models.Model):

    """Model for service a customer subscribed for."""
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider,
                                         on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'''{self.customer} subscribed to
        {self.service_provider.business_name}'''


class Suspension(models.Model):

    """ Model for suspended service providers due to offense"""
    service_provider = models.ForeignKey(ServiceProvider,
                                         on_delete=models.CASCADE)
    suspension_start_date = models.DateTimeField(default=timezone.now)
    suspension_end_date = models.DateTimeField(default=timezone.now)
    suspension_reason = models.CharField(max_length=100)
    offense_discription = models.TextField()

    def __str__(self):
        return f'''{self.service_provider.business_name} suspended from
        {self.suspension_start_date} to {self.suspension_end_date}'''

    def suspension_using_correct_date(self):
        return self.suspension_start_date < self.suspension_end_date

    def suspension_is_over(self):
        return self.suspension_end_date <= timezone.now


class RatingAndReview(models.Model):

    """Model for customer's ratings and reviews."""
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider,
                                         on_delete=models.CASCADE)
    rating = models.CharField(max_length=50, choices=RATINGS,
                              default=RATINGS[1])
    review = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'''{self.service_provider.name} is rated
        {self.rating} by {self.customer.user.username}'''
