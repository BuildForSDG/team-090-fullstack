from django.test import TestCase
from .models import (Service, Category, ServiceProvider,
                     CustomerProfile, Subscription, Suspension)
from cities_light.models import City, Country, Region
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
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

        service_provider = ServiceProvider.objects.create(
                            business_name='Tailor1',
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

        customer_profile = CustomerProfile.objects.create(user=user,
                                                          country=country,
                                                          region=region,
                                                          city=city)

        Subscription.objects.create(customer=customer_profile,
                                    service_provider=service_provider,
                                    date=timezone.now())

    def test_valid_service_model(self):
        service = Service.objects.get(name='Tailoring')
        self.assertEquals(service.name, 'Tailoring')
        self.assertEquals(service.price, 120)

    def test_valid_service_provider_model(self):
        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        self.assertEquals(service_provider.business_name, 'Tailor1')

    def test_customer_profile_model(self):
        user = User.objects.get(first_name='Bello')
        customer_profile = CustomerProfile.objects.get(user=user)
        self.assertEquals(customer_profile.user.first_name, 'Bello')

    def test_valid_subscription_model(self):
        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        subcription = Subscription.objects.get(
                        service_provider=service_provider)
        self.assertNotEquals(
                        subcription.service_provider.business_name, 'Bello')

    def test_invalid_subscription_model(self):
        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        subscription = Subscription.objects.get(
                        service_provider=service_provider)
        self.assertEquals(subscription.service_provider.business_name,
                          'Tailor1')

    def test_valid_suspension_model(self):
        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        suspension = Suspension.objects.create(
            service_provider=service_provider,
            suspension_start_date=timezone.now(),
            suspension_end_date=timezone.now() + datetime.timedelta(days=2))

        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        suspension = Suspension.objects.get(
                        service_provider=service_provider)
        self.assertIs(suspension.suspension_using_correct_date(), True)

    def test_invalid_suspension_model(self):
        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        suspension = Suspension.objects.create(
            service_provider=service_provider,
            suspension_start_date=timezone.now()+datetime.timedelta(days=2),
            suspension_end_date=timezone.now())

        service_provider = ServiceProvider.objects.get(business_name='Tailor1')
        suspension = Suspension.objects.get(
                        service_provider=service_provider)
        self.assertIs(suspension.suspension_using_correct_date(), False)
