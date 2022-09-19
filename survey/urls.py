from rest_framework_nested import routers

from survey.views.survey_view_set import SurveyViewSet

router = routers.DefaultRouter()
router.register('', SurveyViewSet, basename='surveys')

urlpatterns = router.urls
