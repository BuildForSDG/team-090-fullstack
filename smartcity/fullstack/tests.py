from django.test import TestCase
from .models import Service, Category, ServiceProvider
from cities_light.models import City, Country, Region
from django.contrib.auth.models import User
from django.utils import timezone
# Create your tests here.


class ModelTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(first_name='Bello',
                                   last_name='Shehu',
                                   email='bello@yahoo.com')
        country = Country.objects.create(name='Nigeria',
                                         continent='Africa',
                                         phone=234)

        region = Region.objects.create(name_ascii='Borno',
                                       country_id=1,
                                       name='Borno')

        city = City.objects.create(name='Maidugurui',
                                   country=country)

        category = Category.objects.create(
                                           name='Fashion',
                                           document_required=True)

        service = Service.objects.create(name='Tailoring',
                                         price=120, category=category)

        ServiceProvider.objects.create(business_name='Tailor1',
                                       street_address='Adress1',
                                       phone='080333333404',
                                       service_rendered=service,
                                       service_category=category,
                                       picture='image.jpg',
                                       description='Dress for both genders',
                                       years_of_experience=12,
                                       year_of_establishement=timezone.now().date(),
                                       region=region,
                                       city=city,
                                       country=country,
                                       supporting_document='', rating=4,
                                       user=user)

    def test_valid_service_model(self):
        service = Service.objects.get(name='Tailoring')
        self.assertEquals(service.name, 'Tailoring')
        self.assertEquals(service.price, 120)

    def test_valid_service_provider_model(self):
        service_provider = ServiceProvider.objects.get(name='Tailor1')
        self.assertEquals(service_provider.name, 'Tailor1')
