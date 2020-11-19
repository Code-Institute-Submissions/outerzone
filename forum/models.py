from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Forum(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.name