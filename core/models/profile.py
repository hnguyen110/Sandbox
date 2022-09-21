from django.conf import settings
from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    is_disability = models.BooleanField(default=False)
    is_veteran = models.BooleanField(default=False)
    date_of_birth = models.DateTimeField()
    sexual_orientation = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
