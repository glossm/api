from django.contrib import admin
from django.contrib.admin import ModelAdmin

from transcription.admin import ProficiencyInline
from .models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    inlines = [ProficiencyInline]
