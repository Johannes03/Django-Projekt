from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} , {}".format(self.title,self.id)
