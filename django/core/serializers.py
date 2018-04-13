from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Topic, Language, Meaning, Record


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'level')


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class MeaningSerializer(ModelSerializer):
    class Meta:
        model = Meaning
        fields = '__all__'


class RecordSerializer(ModelSerializer):
    language = serializers.CharField(source='language.name')
    meaning = MeaningSerializer()

    class Meta:
        model = Record
        fields = '__all__'
