from django.shortcuts import render
from products.models import Artist

# Create your views here.
def index(request):
    """ View returns the index page """
    artists = Artist.objects.all()
    context = {
        'artists': artists,
    }
    return render(request, 'home/index.html', context)
