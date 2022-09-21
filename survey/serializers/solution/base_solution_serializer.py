from rest_framework.serializers import ModelSerializer

from survey.models.solution import Solution


class BaseSolutionSerializer(ModelSerializer):
    class Meta:
        model = Solution
        fields = ['id', 'description']

    def create(self, validated_data):
        question_id = self.context['question_id']
        return Solution.objects.create(question_id=question_id, **validated_data)
