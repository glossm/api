from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Language, Record
from .serializers import LanguageSerializer, RecordSerializer


class LanguageList(ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class RecordDetail(RetrieveAPIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    lookup_field = 'id'
