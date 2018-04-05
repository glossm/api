from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import UserSerializer


class Profile(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
