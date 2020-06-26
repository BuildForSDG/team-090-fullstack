from django.test import TestCase
from .models import (Service, Category, ServiceProvider,
                     CustomerProfile, Subscription,
                     Suspension, Document,
                     RatingAndReview, MyCity)
from cities_light.models import Country, Region
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from .my_currency import get_currencies_tuple

CURRENCY = get_currencies_tuple()
# Create your tests here.


class ModelTestCase(TestCase):

    """Test case for models."""
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

        city = MyCity.objects.create(city='Maidugurui',
                                   country=country)

        category = Category.objects.create(
                                           name='Fashion',
                                           document_required=True)

        service = Service.objects.create(name='Tailoring',
                                         category=category)

        service_provider = ServiceProvider.objects.create(
                            business_name='Tailor1',
                            street_address='Adress1',
                            phone='080333333404',
                            service_rendered=service,
                            service_category=category,
                            picture='image.jpg',
                            price=200.00,
                            description='Dress for both genders',
                            years_of_experience=12,
                            year_of_establishement=timezone.now().date(),
                            region=region,
                            city=city,
                            country=country,
                            supporting_document='',
                            user=user)

        customer_profile = CustomerProfile.objects.create(user=user,
                                                          country=country,
                                                          region=region,
                                                          city=city)

        Subscription.objects.create(customer=customer_profile,
                                    service_provider=service_provider,
                                    date=timezone.now())
        Document.objects.create(name='CAC')
        RatingAndReview.objects.create(customer=customer_profile,
                                       service_provider=service_provider,
                                       rating='Good',
                                       review='Good service and respectfull',
                                       date=timezone.now())

    def test_valid_service_model(self):
        service = Service.objects.get(name='Tailoring')
        self.assertEquals(service.name, 'Tailoring')

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

    def test_valid_document(self):
        document = Document.objects.get(name='CAC')
        self.assertEquals(document.name, 'CAC')

    def test_invalid_document(self):
        document = Document.objects.get(name='CAC')
        self.assertNotEquals(document.name, 'SSCE')

    def test_valid_ratingreview(self):
        user = User.objects.get(first_name='Bello')
        customer = CustomerProfile.objects.get(user=user)
        rating_and_review = RatingAndReview.objects.get(
            customer_id=customer.id
        )
        self.assertEquals(rating_and_review.customer.user.first_name, 'Bello')
        self.assertEquals(rating_and_review.rating, 'Good')

    def test_invalid_ratingreview(self):
        user = User.objects.get(first_name='Bello')
        customer = CustomerProfile.objects.get(user=user)
        rating_and_review = RatingAndReview.objects.get(
            customer_id=customer.id
        )
        self.assertNotEquals(rating_and_review.customer.user.first_name,
                             'Bashir')
        self.assertNotEquals(rating_and_review.rating, 'Poor')
