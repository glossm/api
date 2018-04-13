from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline

from .models import Submission, Proficiency


@admin.register(Submission)
class SubmissionAdmin(ModelAdmin):
    list_display = (
        '__str__',
        'record',
        'answer',
        'submitter',
    )


class ProficiencyInline(TabularInline):
    model = Proficiency
