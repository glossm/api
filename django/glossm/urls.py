from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import Profile

urlpatterns = [
    path('manage/', admin.site.urls),
    path('profile/', Profile.as_view()),
    path('transcription/', include('transcription.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
