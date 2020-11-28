from django.db import models
from artists.models import Artist


# Create your models here.
class Product(models.Model):
    artist = models.ForeignKey('artists.Artist', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
