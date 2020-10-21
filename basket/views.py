from django.shortcuts import render


# Create your views here.
def view_basket(request):
    """ View returns the shopping basket """

    return render(request, 'basket/basket.html')