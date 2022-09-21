from django.conf import settings
from django.db import models

from survey.models.survey import Survey


class SurveyParticipant(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assigned_surveys')
    status = models.BooleanField(default=True)
