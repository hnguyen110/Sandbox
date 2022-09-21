from django.db import models

from .survey import Survey


class Question(models.Model):
    description = models.TextField(null=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    type = models.CharField(max_length=255, null=False)
