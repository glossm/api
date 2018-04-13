from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView

from .models import Language
from .serializers import TopicSerializer, LanguageSerializer, RecordSerializer


class TopicList(ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        language = get_object_or_404(Language, code=self.kwargs['code'])
        topics = language.topic_set.topics
        return topics.order_by('level', 'name')


class LanguageList(ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class RecordList(ListAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        language = get_object_or_404(Language, code=self.kwargs['code'])
        topic_id = self.kwargs['topic_id']
        topic = language.topic_set.topics.filter(id=topic_id).first()
        if topic is None:
            raise NotFound
        return language.records.filter(meaning__in=topic.meanings.all())
