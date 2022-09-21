from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from survey.models.survey_participant import SurveyParticipant
from survey.serializers.survey_participant.base_survey_participant_serializer import BaseSurveyParticipantSerializer


class SurveyParticipantViewSet(ModelViewSet):
    queryset = SurveyParticipant.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BaseSurveyParticipantSerializer

    def get_serializer_context(self):
        return {
            'survey_id': self.kwargs['survey_pk']
        }
