from django.shortcuts import render


# Create your views here.
def forum(request):
    """ Returns the forum page """
    context = {
    }
    return render(request, 'forum/index.html', context)
