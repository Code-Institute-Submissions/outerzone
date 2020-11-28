from django.contrib import admin
from .models import Product
from artists.models import Artist


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'artist',
        'price',
        'image'
    )
    ordering = ('artist',)

admin.site.register(Product, ProductAdmin)

