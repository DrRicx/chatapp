from django.db import models
from datetime import datetime


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    userMessage = models.CharField(max_length=250, null=False, blank=False)
    date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    user = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.userMessage[0:50]
