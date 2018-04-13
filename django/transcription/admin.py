from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(ModelAdmin):
    list_display = (
        '__str__',
        'record',
        'answer',
        'submitter',
    )
