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


class Event(models.Model):
    artist = models.ForeignKey('Artist', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name