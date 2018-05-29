from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Language
from .serializers import TopicSerializer, LanguageSerializer, RecordSerializer


class TopicList(ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        language = get_object_or_404(Language, id=self.kwargs['id'])
        topics = language.topic_set.topics
        return topics.order_by('level', 'name')

    def get_serializer_context(self):
        return {'request': self.request, 'language_id': self.kwargs['id']}


class LanguageList(ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class LanguageDetail(RetrieveAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()
    lookup_field = 'id'


class RecordList(ListAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        language = get_object_or_404(Language, id=self.kwargs['lang_id'])
        topic_id = self.kwargs['topic_id']
        topic = language.topic_set.topics.filter(id=topic_id).first()
        if topic is None:
            raise NotFound
        return language.records.filter(meaning__in=topic.meanings.all())
