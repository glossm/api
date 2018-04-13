from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Record
from .models import Submission


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
