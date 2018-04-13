from rest_framework.generics import CreateAPIView

from .models import Submission
from .serializers import SubmissionSerializer, ProficiencySerializer


class SubmissionCreate(CreateAPIView):
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()


class ProficiencyCreate(CreateAPIView):
    serializer_class = ProficiencySerializer

    def get_queryset(self):
        return self.request.user.proficiency
