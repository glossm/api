from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from sorl.thumbnail.fields import ImageField

from glossm.settings import LANGUAGES


class User(AbstractUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=100, blank=True)
    nationality = CountryField(blank=True, null=True)
    profile_image = ImageField(upload_to='profiles', blank=True, null=True)

    preferred_language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    is_expert = models.BooleanField(default=False)
    exp = models.PositiveIntegerField('EXP', default=0)

    def get_full_name(self):
        return self.name

    def level(self):
        return int(self.exp / 100) + 1
