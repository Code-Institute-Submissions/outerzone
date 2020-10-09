from django.contrib import admin
from .models import Product


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
