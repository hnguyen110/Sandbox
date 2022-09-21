from django.conf import settings
from django.db import models


class Survey(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='surveys')
