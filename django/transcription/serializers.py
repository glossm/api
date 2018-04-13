from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

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
        record = validated_data['record']
        submission = Submission.objects.create(
            submitter=user,
            record=record,
            answer=validated_data['answer'],
        )
        proficiency = user.proficiency.filter(language=record.language).first()
        if proficiency is None:
            raise ValidationError('You are not learning this language.')
        proficiency.exp += submission.score()
        proficiency.save()
        return submission

    def get_top_answers(self, submission):
        return submission.record.top_answers()
