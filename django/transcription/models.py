from django.db import models
from django.db.models import Model, PROTECT

from accounts.models import User
from core.models import Language, Record


class Submission(Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    record = models.ForeignKey(Record, PROTECT, related_name='submissions')
    submitter = models.ForeignKey(User, PROTECT, related_name='submissions')
    answer = models.CharField(max_length=100)

    class Meta:
        db_table = 'Submission'

    def __str__(self):
        return f'Submission #{self.id}'

    def score(self):
        # TODO: Calculate similarity-based scores
        return len(self.answer)


class Proficiency(Model):
    user = models.ForeignKey(User, PROTECT, related_name='proficiency')
    language = models.ForeignKey(Language, PROTECT, related_name='proficiency')
    exp = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'Proficiency'
        unique_together = ('user', 'language')
        verbose_name_plural = 'Proficiency'

    def __str__(self):
        return f"{self.user}'s proficiency in {self.language}"
