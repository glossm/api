from django.urls import path

from .views import LanguageList, RecordDetail, SubmissionCreate

urlpatterns = [
    path('languages/', LanguageList.as_view()),
    path('records/<int:id>/', RecordDetail.as_view()),
    path('submissions/', SubmissionCreate.as_view()),
]
