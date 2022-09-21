from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from survey.models.solution import Solution
from survey.serializers.solution.base_solution_serializer import BaseSolutionSerializer


class SolutionViewSet(ModelViewSet):
    queryset = Solution.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BaseSolutionSerializer

    def get_serializer_context(self):
        return {
            'question_id': self.kwargs['question_pk']
        }
