from django.urls import path

from .views import SubmissionCreate

urlpatterns = [
    path('submit/', SubmissionCreate.as_view()),
]
