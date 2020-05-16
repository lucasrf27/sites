from django.db import models
from datetime import datetime

# Create your models here.
class Car(models.Model):
    YEAR_CHOICES = []
    for r in range(1960, (datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    brand = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.now().year)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cars'
        ordering = ["brand"]
