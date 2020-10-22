from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 3.95

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context