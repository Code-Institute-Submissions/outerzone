from django.contrib import admin
from .models import Product, Artist


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'name',
        'artist',
        'price',
    )
    ordering = ('artist',)

class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
    )
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Artist, ArtistAdmin)
