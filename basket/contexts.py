from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    delivery = 3.95
    basket = request.session.get('basket', {})
    grand_total = 0

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        sub_total = quantity * product.price
        total += sub_total
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'sub_total': sub_total,
            'total': total,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context