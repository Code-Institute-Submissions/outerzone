from django.test import TestCase
from .forms import ArtistForm

class TestArtistForm(TestCase):

    def test_artist_name_required(self):
        form = ArtistForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_all_other_fields_not_required(self):
        form = ArtistForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())
