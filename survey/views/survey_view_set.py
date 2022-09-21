from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from survey.models.survey import Survey
from survey.serializers.survey.base_survey_serializer import BaseSurveySerializer
from survey.serializers.survey.modify_survey_serializer import ModifySurveySerializer


class SurveyViewSet(ModelViewSet):
    http_method_names = ['post', 'get', 'put', 'patch', 'delete', 'head', 'options']
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Survey.objects.filter(owner=self.request.user).prefetch_related('questions__solutions')

    def get_serializer_context(self):
        return {
            'user': self.request.user,
            'survey_id': self.kwargs['pk'] if 'pk' in self.kwargs else 0
        }

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return ModifySurveySerializer
        return BaseSurveySerializer
