from django.urls import path

from .views import TopicList, LanguageList, LanguageDetail, RecordList

urlpatterns = [
    path('languages/', LanguageList.as_view()),
    path('languages/<int:id>/', LanguageDetail.as_view()),
    path('languages/<int:id>/topics/', TopicList.as_view()),
    path('languages/<int:lang_id>/topics/<int:topic_id>/records/', RecordList.as_view()),
]
