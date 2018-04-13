from django.contrib.humanize.templatetags.humanize import intword
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Count, Model, PROTECT
from django.db.models.functions import Cast


class Language(Model):
    EGID_SCALE = (
        ('0', 'International (0)'),
        ('1', 'National (1)'),
        ('2', 'Provincial (2)'),
        ('3', 'Wider Communication (3)'),
        ('4', 'Educational (4)'),
        ('5', 'Developing (5)'),
        ('6a', 'Vigorous (6a)'),
        ('6b', 'Threatened (6b)'),
        ('7', 'Shifting (7)'),
        ('8a', 'Moribund (8a)'),
        ('8b', 'Nearly Extinct (8b)'),
        ('9', 'Dormant (9)'),
        ('10', 'Extinct (10)'),
    )

    code = models.CharField(
        unique=True,
        max_length=3,
        validators=[MinLengthValidator(2)],
    )
    name = models.CharField(max_length=50)
    num_speakers = models.PositiveIntegerField('number of speakers')
    endangerment = models.CharField(max_length=2, choices=EGID_SCALE)

    class Meta:
        db_table = 'Language'

    def __str__(self):
        return self.name

    def number_of_speakers(self):
        return intword(self.num_speakers)


class Meaning(Model):
    ask_code = models.CharField(
        'ASK code',
        unique=True,
        max_length=5,
        validators=[MinLengthValidator(5)],
    )
    in_en = models.CharField('in English', max_length=100)
    in_ko = models.CharField('in Korean', max_length=100)
    in_ru = models.CharField('in Russian', max_length=100)
    in_zh = models.CharField('in Chinese', max_length=100)
    in_mn = models.CharField('in Mongolian', max_length=100)
    note = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'Meaning'

    def __str__(self):
        return '{} ({})'.format(self.ask_code, self.in_en)


class Record(Model):
    language = models.ForeignKey(Language, PROTECT, related_name='records')
    meaning = models.ForeignKey(Meaning, PROTECT, related_name='records')
    audio = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'Record'
        unique_together = ('language', 'meaning')

    def __str__(self):
        return 'Record #{}'.format(self.id)

    def top_answers(self, select=5):
        total = self.submissions.count()
        answers = self.submissions.values('answer')
        answer_stats = answers.annotate(percent=Cast(Count('answer'), models.FloatField()) * 100 / total)
        return answer_stats.order_by('-percent')[:select]
