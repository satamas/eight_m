from __future__ import unicode_literals

from datetime import datetime
from django.db import models


# Create your models here.

class Team(models.Model):
    sides = [
        (0, 'dark'),
        (1, 'light')
    ]
    side = models.CharField(max_length=1, choices=sides)


class Wins(models.Model):
    name = models.CharField(max_length=500)
    timestamp = models.DateTimeField(default=datetime.now())
    team = models.ForeignKey(Team)
