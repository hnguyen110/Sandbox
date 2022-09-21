from rest_framework.serializers import ModelSerializer

from survey.models.answer import Answer
from survey.serializers.question.answered_question_serializer import AnsweredQuestionSerializer
from survey.serializers.solution.base_solution_serializer import BaseSolutionSerializer


class BaseAnswerSerializer(ModelSerializer):
    question = AnsweredQuestionSerializer(read_only=True)
    solution = BaseSolutionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'description', 'question', 'solution']
