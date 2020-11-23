from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product
from artists.models import Artist
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """ View returns all products """
    products = Product.objects.all()
    artists = Artist.objects.all()
    filterArtists = None
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'artist' in request.GET:
            filterArtists = request.GET['artist'].split(',')
            products = products.filter(artist__name__in=filterArtists)
            filterArtists = Artist.objects.filter(name__in=artists)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'Please enter search term')
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(artist__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'artists': artists,
        'search_term': query,
        'current_artists': artists,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ View returns detail for each product """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Superuser can add a product """
    if not request.user.is_superuser:
        messages.error(request, 'No access for non-admin users')
        return redirect(reverse('home'))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product not yet added. Please check your form.')
    else:
        form=ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Superuser can edit a product """
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'No access for non-admin users')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product udpated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Update failed. Please check your form')
    else:
        form=ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Superuser can delete product """
    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'No access for non-admin users')
        return redirect(reverse('home'))

    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
