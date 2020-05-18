from django.db import models

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