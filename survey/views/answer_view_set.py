from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from survey.models.answer import Answer
from survey.serializers.answer.base_answer_serializer import BaseAnswerSerializer
from survey.serializers.answer.modify_answer_serializer import ModifyAnswerSerializer


class AnswerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT']:
            return ModifyAnswerSerializer
        return BaseAnswerSerializer

    def get_queryset(self):
        return Answer \
            .objects \
            .prefetch_related('solution') \
            .prefetch_related('question') \
            .filter(participant_id=self.kwargs['participant_pk'])

    def get_serializer_context(self):
        return {
            'participant_id': self.kwargs['participant_pk']
        }
