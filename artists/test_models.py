from django.test import TestCase
from .models import Artist, Event 

class TestModels(TestCase):

    def test_artist_string_method_returns_name(self):
        artist = Artist.objects.create(name='Test Artist')
        self.assertEqual(str(artist), 'Test Artist')