from django.db import models
from datetime import date

class Note(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(default=date.today)
