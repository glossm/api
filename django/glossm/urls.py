from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('', RedirectView.as_view(url='manage/')),
    path('manage/', admin.site.urls),
    path('accounts/', include('rest_auth.urls')),
    path('accounts/registration/', include('rest_auth.registration.urls')),
    path('accounts/token/refresh/', refresh_jwt_token),
    path('accounts/token/verify/', verify_jwt_token),
    path('core/', include('core.urls')),
    path('transcription/', include('transcription.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
