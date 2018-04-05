from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Language, Meaning, Record, Submission


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
        'in_en',
        'in_ko',
        'in_ru',
        'in_zh',
        'in_mn',
        'note',
    )


@admin.register(Record)
class RecordAdmin(ModelAdmin):
    list_display = (
        '__str__',
        'language',
        'meaning',
    )


@admin.register(Submission)
class SubmissionAdmin(ModelAdmin):
    list_display = (
        '__str__',
        'record',
        'answer',
        'submitter',
    )
