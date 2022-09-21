from rest_framework.serializers import ModelSerializer

from survey.models.question import Question


class BaseQuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'type', 'description']

    def create(self, validated_data):
        survey_id = self.context['survey_id']
        return Question.objects.create(survey_id=survey_id, **validated_data)
