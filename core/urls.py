from django.urls import path

from core.views.profile_view_set import ProfileView

urlpatterns = [
    path('', ProfileView.as_view())
]
