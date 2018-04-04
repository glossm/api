from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import User


@admin.register(User)
class UserAdmin(ModelAdmin):
    pass
