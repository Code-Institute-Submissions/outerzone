from django.test import TestCase
from django.urls import reverse
from .models import Artist
from . import views

# Create your tests here.
class TestViews(TestCase):
    def test_get_all_artists(self):
        response = self.client.get('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/all_artists.html')

    def test_get_artist_detail(self):
        artist = Artist.objects.create(name='Test Artist')
        response = self.client.get(f'/artists/{artist.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'artists/artist_detail.html')
    
    def test_login_required_for_add_artist(self):
        response = self.client.get(reverse('add_artist'))
        artist = Artist.objects.create(name='Test Artist')
        self.assertRedirects(response, '/accounts/login/?next=/artists/add/')
    
    # def test_superuser_login_required_for_add_artist(self):
    #     self.client.login(username='username', password='password')
    #     response = self.client.get(reverse('add_artist'))
    #     self.assertRedirects(response, '/')