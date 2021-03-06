from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from sorl.thumbnail.fields import ImageField

from core.models import Language
from glossm.settings import LANGUAGES
from glossm.utils import RenamedPath


class User(AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=100, blank=True)
    nationality = CountryField(blank=True, null=True)
    profile_image = ImageField(upload_to=RenamedPath('profile_images', 'user'), blank=True, null=True)

    preferred_language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    is_expert = models.BooleanField(default=False)
    learning_languages = models.ManyToManyField(Language, through='transcription.Proficiency')

    class Meta:
        db_table = 'User'

    def save(self, *args, **kwargs):
        if self.id is None:
            profile_image = self.profile_image
            self.profile_image = None
            super().save(*args, **kwargs)
            self.profile_image = profile_image
        super().save(*args, **kwargs)

    def get_full_name(self):
        return self.name
