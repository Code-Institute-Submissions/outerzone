from django.contrib import admin
from .models import Artist , Event

# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'image',
    )
    ordering = ('name',)


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'location',
        'date',
    )
    order = ('date',)

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Event, EventAdmin)