from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    grand_total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        sub_total = quantity * product.price
        grand_total += sub_total
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'sub_total': sub_total,
        })

    context = {
        'basket_items': basket_items,
        'product_count': product_count,
        'sub_total': sub_total,
        'grand_total': grand_total,
    }

    return context