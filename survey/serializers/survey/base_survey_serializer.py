from rest_framework import serializers

from survey.models.survey import Survey
from survey.serializers.question.base_question_serializer import BaseQuestionSerializer


class BaseSurveySerializer(serializers.ModelSerializer):
    questions = BaseQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ['id', 'name', 'description', 'questions']
