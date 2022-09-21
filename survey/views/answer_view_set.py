from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from survey.models.answer import Answer
from survey.serializers.answer.base_answer_serializer import BaseAnswerSerializer


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BaseAnswerSerializer

    def get_serializer_context(self):
        return {
            'participant_id': self.kwargs['participant_pk']
        }
