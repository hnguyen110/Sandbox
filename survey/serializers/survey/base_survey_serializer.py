from rest_framework import serializers

from survey.models.survey import Survey


class BaseSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'name', 'description']
