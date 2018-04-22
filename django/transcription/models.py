from django.db import models
from django.db.models import Model, PROTECT

from accounts.models import User
from core.models import Language, Record


def get_distance(str1, str2):
    # Calculate the Levenshtein distance between two strings
    len1, len2 = len(str1), len(str2)
    prev = range(len2 + 1)
    for row in range(len1):
        curr = [row + 1] * (len2 + 1)
        for col in range(len2):
            deletion_cost = prev[col + 1] + 1
            insertion_cost = curr[col] + 1
            substitution_cost = prev[col] if str1[row] == str2[col] else prev[col] + 1
            curr[col + 1] = min(deletion_cost, insertion_cost, substitution_cost)
        prev = curr
    return prev[len2]


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
        full_score = 10
        top_answer_stats = self.record.top_answers(10)
        demerits = []
        for stat in top_answer_stats:
            answer, ratio = stat['answer'], stat['ratio']
            max_distance = max(len(self.answer), len(answer))
            demerit = get_distance(self.answer, answer) / max_distance
            demerits.append(demerit * ratio)
        return round(full_score * (1 - sum(demerits)))


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
