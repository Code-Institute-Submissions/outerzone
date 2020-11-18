from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    discogs = models.URLField(max_length=1050, null=True, blank=True)
    soundcloud = models.URLField(max_length=1050, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    artist = models.ForeignKey('Artist', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
