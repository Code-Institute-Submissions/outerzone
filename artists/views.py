from django.shortcuts import render, get_object_or_404
from .models import Artist, Event
from products.models import Product

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
    all_products = Product.objects.all()
    all_events = Event.objects.all()

    products = all_products.filter(artist__name = artist)
    events = all_events.filter(artist__name = artist)

    context = {
        'artist': artist,
        'products': products,
        'events': events,
    }
    return render(request, 'artists/artist_detail.html', context)