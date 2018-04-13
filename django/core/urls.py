from django.urls import path

from .views import TopicList, LanguageList, RecordDetail

urlpatterns = [
    path('languages/', LanguageList.as_view()),
    path('languages/<str:code>/topics/', TopicList.as_view()),
    path('records/<int:id>/', RecordDetail.as_view()),
]
