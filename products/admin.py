from django.contrib import admin
from .models import Product
from artists.models import Artist


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'artist',
        'price',
    )
    ordering = ('artist',)

admin.site.register(Product, ProductAdmin)

