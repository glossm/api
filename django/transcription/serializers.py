from django.db.utils import IntegrityError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

from core.models import Language, Record
from .models import Submission, Proficiency


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

    @staticmethod
    def get_top_answers(submission):
        return submission.record.top_answers()


class ProficiencySerializer(ModelSerializer):
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())

    class Meta:
        model = Proficiency
        fields = ('language', 'exp')
        read_only_fields = ('exp',)

    def create(self, validated_data):
        user = self.context['request'].user
        language = validated_data['language']
        try:
            proficiency = Proficiency.objects.create(user=user, language=language)
            return proficiency
        except IntegrityError:
            raise ValidationError('You are already learning this language.')
