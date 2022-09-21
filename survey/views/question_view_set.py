from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from survey.models.question import Question
from survey.serializers.question.base_question_serializer import BaseQuestionSerializer


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BaseQuestionSerializer

    def get_serializer_context(self):
        return {
            'survey_id': self.kwargs['survey_pk']
        }
