from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from import_export.resources import ModelResource

from .models import TopicSet, Topic, Language, Meaning, Record


class CustomIEModelAdmin(ImportExportModelAdmin):
    def get_import_formats(self):
        formats = (base_formats.CSV,)
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (base_formats.CSV,)
        return [f for f in formats if f().can_export()]


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


class MeaningResource(ModelResource):
    class Meta:
        model = Meaning
        exclude = ('id',)
        import_id_fields = ('ask_code',)


@admin.register(Meaning)
class MeaningAdmin(CustomIEModelAdmin):
    resource_class = MeaningResource
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
