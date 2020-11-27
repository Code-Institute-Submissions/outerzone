from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from . import views


# Create your tests here.
class TestViews(TestCase):
    def test_view_basket(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
    
    # def test_add_to_basket(self):
    #     product = Product.objects.create(name='Test Product', pk=1, price='20')
    #     response = self.client.post('/basket/', {'quantity': 5})
    #     self.assertEqual('basket', {'product': 1, 'quantity': 5, 'price': '20'})