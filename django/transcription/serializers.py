from rest_framework import serializers
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
    top_answers = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = (
            'record',
            'answer',
            'score',
            'top_answers',
        )

    def create(self, validated_data):
        user = self.context['request'].user
        submission = Submission.objects.create(
            submitter=user,
            record=validated_data['record'],
            answer=validated_data['answer'],
        )
        user.exp += submission.score()
        user.save()
        return submission

    def get_top_answers(self, submission):
        return submission.record.top_answers()
