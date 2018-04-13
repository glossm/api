from django.urls import path

from .views import SubmissionCreate, ProficiencyCreate

urlpatterns = [
    path('submit/', SubmissionCreate.as_view()),
    path('start-learning/', ProficiencyCreate.as_view()),
]
