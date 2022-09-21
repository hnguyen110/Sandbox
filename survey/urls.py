from rest_framework_nested import routers

from survey.views.question_view_set import QuestionViewSet
from survey.views.solution_view_set import SolutionViewSet
from survey.views.survey_view_set import SurveyViewSet

router = routers.DefaultRouter()
router.register('', SurveyViewSet, basename='surveys')
surveys_router = routers.NestedDefaultRouter(router, '', lookup='survey')
surveys_router.register('questions', QuestionViewSet, basename='survey-questions')
questions_router = routers.NestedDefaultRouter(surveys_router, 'questions', lookup='question')
questions_router.register('solutions', SolutionViewSet, basename='question-solutions')

urlpatterns = router.urls + surveys_router.urls + questions_router.urls
