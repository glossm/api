from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('manage/', admin.site.urls),
]
