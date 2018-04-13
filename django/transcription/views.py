from rest_framework.generics import CreateAPIView

from .models import Submission
from .serializers import SubmissionSerializer


class SubmissionCreate(CreateAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()
