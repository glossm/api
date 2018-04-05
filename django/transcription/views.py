from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from .models import Language, Record, Submission
from .serializers import LanguageSerializer, RecordSerializer, SubmissionSerializer


class LanguageList(ListAPIView):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class RecordDetail(RetrieveAPIView):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()
    lookup_field = 'id'


class SubmissionCreate(CreateAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
