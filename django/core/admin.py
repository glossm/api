from django.contrib import admin
from django.contrib.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.formats import base_formats
from import_export.resources import ModelResource
from import_export.widgets import ForeignKeyWidget

from .models import TopicSet, Topic, Language, Meaning, Informant, Record


class CustomIEModelAdmin(ImportExportModelAdmin):
    def get_import_formats(self):
        formats = (base_formats.CSV,)
        return [f for f in formats if f().can_import()]

    def get_export_formats(self):
        formats = (base_formats.CSV,)
        return [f for f in formats if f().can_export()]


class TopicSetResource(ModelResource):
    class Meta:
        model = TopicSet
        exclude = ('id',)
        import_id_fields = ('code',)


@admin.register(TopicSet)
class TopicSetAdmin(CustomIEModelAdmin):
    resource_class = TopicSetResource
    list_display = ('name',)


class TopicResource(ModelResource):
    topic_set = Field(
        column_name='topic_set',
        attribute='topic_set',
        widget=ForeignKeyWidget(TopicSet, 'code'),
    )

    class Meta:
        model = Topic
        exclude = ('id',)
        import_id_fields = ('code',)


@admin.register(Topic)
class TopicAdmin(CustomIEModelAdmin):
    resource_class = TopicResource
    list_display = (
        'name',
        'level',
        'topic_set',
    )


class LanguageResource(ModelResource):
    topic_set = Field(
        column_name='topic_set',
        attribute='topic_set',
        widget=ForeignKeyWidget(TopicSet, 'code'),
    )

    class Meta:
        model = Language
        exclude = ('id',)
        import_id_fields = ('code',)


@admin.register(Language)
class LanguageAdmin(CustomIEModelAdmin):
    resource_class = LanguageResource
    list_display = (
        'name',
        'code',
        'number_of_speakers',
    )


class MeaningResource(ModelResource):
    topic = Field(
        column_name='topic',
        attribute='topic',
        widget=ForeignKeyWidget(Topic, 'code'),
    )

    class Meta:
        model = Meaning
        exclude = ('id',)
        import_id_fields = ('ask_code',)


@admin.register(Informant)
class Informantdmin(CustomIEModelAdmin):
    list_display = (
        'code',
        'language',
        'full_name',
        'gender',
        'date_of_birth',
    )


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
