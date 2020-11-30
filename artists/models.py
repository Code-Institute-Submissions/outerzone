from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=300)
    display_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    youtube_url = models.URLField(max_length=1050, null=True, blank=True)
    discogs_url = models.URLField(max_length=1050, null=True, blank=True)
    soundcloud_url = models.URLField(max_length=1050, null=True, blank=True)
    facebook_url = models.URLField(max_length=1050, null=True, blank=True)
    instagram_url = models.URLField(max_length=1050, null=True, blank=True)
    resident_advisor_url = models.URLField(
        max_length=1050, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Event(models.Model):
    artist = models.ForeignKey(
        'Artist', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name
