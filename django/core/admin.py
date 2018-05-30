from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import TopicSet, Topic, Language, Meaning, Record


@admin.register(TopicSet)
class TopicSetAdmin(ModelAdmin):
    list_display = ('name',)


@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    list_display = (
        'name',
        'level',
        'topic_set',
    )


@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = (
        'name',
        'code',
        'number_of_speakers',
    )


@admin.register(Meaning)
class MeaningAdmin(ModelAdmin):
    list_display = (
        'ask_code',
        'en',
        'ko',
        'ru',
        'zh',
        'mn',
        'note',
    )


@admin.register(Record)
class RecordAdmin(ModelAdmin):
    list_display = (
        '__str__',
        'language',
        'meaning',
    )
