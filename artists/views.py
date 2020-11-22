from django.shortcuts import render, get_object_or_404
from products.models import Artist

# Create your views here.
def all_artists(request):
    """ View all artists """
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(request, 'artists/all_artists.html', context)


def artist_detail(request, artist_id):
    """ View for each artist """
    artist = get_object_or_404(Artist, pk=artist_id)
    context = {
        'artist': artist,
    }
    return render(request, 'artists/artist_detail.html', context)