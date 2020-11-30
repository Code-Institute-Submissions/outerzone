from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Artist, Event
from .forms import ArtistForm
from products.models import Product


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
    products = all_products.filter(artist__name=artist)
    events = all_events.filter(artist__name=artist)
    context = {
        'artist': artist,
        'products': products,
        'events': events,
    }
    return render(request, 'artists/artist_detail.html', context)


@login_required
def add_artist(request):
    """ Superuser can add artist """
    if not request.user.is_superuser:
        messages.error(request, 'No access for non-admin users')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            artist = form.save()
            messages.success(request, 'Artist added')
            return redirect(reverse('artist_detail', args=[artist.id]))
        else:
            messages.error(
                request, 'Artist not yet added. Please check your form.')
    else:
        form = ArtistForm()

    form = ArtistForm()
    template = 'artists/add_artist.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
