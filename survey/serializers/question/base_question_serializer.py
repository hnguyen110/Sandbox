from rest_framework.serializers import ModelSerializer

from survey.models.question import Question
from survey.serializers.solution.base_solution_serializer import BaseSolutionSerializer


class BaseQuestionSerializer(ModelSerializer):
    solutions = BaseSolutionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'type', 'description', 'solutions']

    def create(self, validated_data):
        survey_id = self.context['survey_id']
        return Question.objects.create(survey_id=survey_id, **validated_data)
