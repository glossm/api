from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Topic, Language, Meaning, Informant, Record


class TopicSerializer(ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ('id', 'name', 'level', 'progress')

    def get_progress(self, topic):
        submissions = self.context['request'].user.submissions
        language = Language.objects.get(id=self.context['language_id'])
        records = language.records.filter(meaning__in=topic.meanings.all())
        learned_status = [submissions.filter(record=record).exists() for record in records]
        return {'current': sum(learned_status), 'total': records.count()}


class LanguageSerializer(ModelSerializer):
    learning = serializers.SerializerMethodField()

    class Meta:
        model = Language
        fields = '__all__'

    def get_learning(self, language):
        user = self.context['request'].user
        return user.proficiency.filter(language=language).exists()


class MeaningSerializer(ModelSerializer):
    class Meta:
        model = Meaning
        fields = '__all__'


class InformantSerializer(ModelSerializer):
    class Meta:
        model = Informant
        fields = '__all__'


class RecordSerializer(ModelSerializer):
    meaning = MeaningSerializer()
    learned = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = (
            'id',
            'meaning',
            'audio',
            'video',
            'learned',
        )

    def get_learned(self, record):
        user = self.context['request'].user
        submissions = user.submissions.filter(record=record)
        return submissions.exists()
