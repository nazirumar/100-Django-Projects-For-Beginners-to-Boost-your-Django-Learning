from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Room(models.Model):
    name = models.CharField(max_length=100)
    userslist =models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)


class Message(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "chat_message"
        ordering = ("timestamp",)