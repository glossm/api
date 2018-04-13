from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Language, Record
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


class RecordDetail(RetrieveAPIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    lookup_field = 'id'
