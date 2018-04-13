from django.urls import path

from .views import LanguageList, RecordDetail

urlpatterns = [
    path('languages/', LanguageList.as_view()),
    path('records/<int:id>/', RecordDetail.as_view()),
]
