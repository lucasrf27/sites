from django.db import models


class To_do (models.Model):
    task = models.CharField(max_length=150)
    topic = models.CharField(max_length=150)
    how = models.TextField(max_length=600)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=False)
    updated_at = models.DateTimeField(auto_now=True)
    ONGOING = 'OG'
    LEARN = 'LN'
    field_choices = [
        (ONGOING, 'ONGOING'),
        (LEARN, 'LEARN'),
    ]
    status1 = models.CharField(choices=field_choices, max_length=2, default=LEARN)

    def __str__(self):
        return self.task
