from django.db import models

from .question import Question


class Solution(models.Model):
    description = models.TextField(null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='solutions')
