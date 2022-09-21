from rest_framework.serializers import ModelSerializer

from survey.models.answer import Answer


class ModifyAnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'description', 'question', 'solution']

    def create(self, validated_data):
        participant_id = self.context['participant_id']
        return Answer.objects.create(participant_id=participant_id, **validated_data)
