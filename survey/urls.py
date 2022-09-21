from rest_framework_nested import routers

from survey.views.answer_view_set import AnswerViewSet
from survey.views.question_view_set import QuestionViewSet
from survey.views.solution_view_set import SolutionViewSet
from survey.views.survey_participant_view_set import SurveyParticipantViewSet
from survey.views.survey_view_set import SurveyViewSet

router = routers.DefaultRouter()
router.register('surveys', SurveyViewSet, basename='surveys')

surveys_router = routers.NestedDefaultRouter(router, 'surveys', lookup='survey')
surveys_router.register('questions', QuestionViewSet, basename='survey-questions')
surveys_router.register('participants', SurveyParticipantViewSet, basename='survey-participants')

questions_router = routers.NestedDefaultRouter(surveys_router, 'questions', lookup='question')
questions_router.register('solutions', SolutionViewSet, basename='question-solutions')

participants_router = routers.NestedDefaultRouter(surveys_router, 'participants', lookup='participant')
participants_router.register('answers', AnswerViewSet, basename='participant-answers')

urlpatterns = router.urls + surveys_router.urls + questions_router.urls + participants_router.urls
