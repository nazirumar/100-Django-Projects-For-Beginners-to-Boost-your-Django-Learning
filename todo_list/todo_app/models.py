from django.db import models
from django.contrib.auth.models import User

# Create your models here.


_DONE= (
   ( 'primary','primary'),
   ('read', 'red'),
)

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=500)
    is_reading = models.BooleanField(default=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title