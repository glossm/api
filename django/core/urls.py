from django.urls import path

from .views import TopicList, LanguageList, RecordList

urlpatterns = [
    path('languages/', LanguageList.as_view()),
    path('languages/<str:code>/topics/', TopicList.as_view()),
    path('languages/<str:code>/topics/<int:topic_id>/records', RecordList.as_view()),
]
