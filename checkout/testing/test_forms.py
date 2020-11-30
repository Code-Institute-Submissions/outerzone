from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_full_name_required(self):
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_required(self):
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_phone_number_required(self):
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_required(self):
        form = OrderForm({'country': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['country'][0], 'This field is required.')

    def test_town_or_city_required(self):
        form = OrderForm({'town_or_city': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address1_required(self):
        form = OrderForm({'street_address1': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')
