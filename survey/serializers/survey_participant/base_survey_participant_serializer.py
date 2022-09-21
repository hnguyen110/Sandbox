from rest_framework.serializers import ModelSerializer

from survey.models.survey_participant import SurveyParticipant


class BaseSurveyParticipantSerializer(ModelSerializer):
    class Meta:
        model = SurveyParticipant
        fields = ['id', 'user', 'status']

    def create(self, validated_data):
        survey_id = self.context['survey_id']
        return SurveyParticipant.objects.create(survey_id=survey_id, **validated_data)
