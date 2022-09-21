from django.conf import settings
from django.db import models

from survey.models.question import Question
from survey.models.solution import Solution
from survey.models.survey_participant import SurveyParticipant


class Answer(models.Model):
    description = models.TextField(null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL, related_name='participant_answers')
    solution = models.ForeignKey(Solution, null=True, on_delete=models.SET_NULL, related_name='participant_answers')
    participant = models.ForeignKey(SurveyParticipant, on_delete=models.CASCADE, related_name='answers')
