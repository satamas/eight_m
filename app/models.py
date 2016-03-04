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


class Event(models.Model):
    name = models.CharField(max_length=500)


class Wins(models.Model):
    team = models.ForeignKey(Team)
    timestamp = models.DateTimeField(default=datetime.now())
    event = models.ForeignKey(Event)
    rate = models.IntegerField(null=True, default=None)
