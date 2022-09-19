from django.db import transaction
from rest_framework import serializers

from survey.models.survey import Survey


class ModifySurveySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_null=False)
    description = serializers.CharField(allow_null=False)

    def update(self, instance, validated_data):
        with transaction.atomic():
            name = self.validated_data['name']
            description = self.validated_data['description']
            survey = Survey.objects.get(pk=self.context['survey_id'])
            survey.name = name
            survey.description = description
            survey.save()
            return survey

    def create(self, validated_data):
        with transaction.atomic():
            name = self.validated_data['name']
            description = self.validated_data['description']
            survey = Survey.objects.create(name=name, description=description, user=self.context['user'])
            return survey
