from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from rest_framework.serializers import ModelSerializer

from .models import Language, Meaning, Record, Submission


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


class SubmissionSerializer(ModelSerializer):
    record = serializers.PrimaryKeyRelatedField(queryset=Record.objects.all())

    class Meta:
        model = Submission
        fields = (
            'record',
            'answer',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        if not user.is_authenticated:
            raise NotAuthenticated
        submission = Submission.objects.create(
            submitter=user,
            record=validated_data['record'],
            answer=validated_data['answer'],
        )
        return submission
