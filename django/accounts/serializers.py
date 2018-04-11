from django_countries.serializers import CountryFieldMixin
from rest_framework.serializers import ModelSerializer
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import User


class UserSerializer(CountryFieldMixin, ModelSerializer):
    profile_thumbnail = HyperlinkedSorlImageField(
        '128x128',
        source='profile_image',
        options={'crop': 'center'},
        read_only=True,
    )

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'nationality',
            'profile_thumbnail',
            'preferred_language',
            'is_expert',
            'level',
        )
