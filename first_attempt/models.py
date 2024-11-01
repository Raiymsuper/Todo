from datetime import *
from django.utils import timezone

from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length= 128)
    description = models.TextField()
    completed = models.BooleanField()
    deadline = models.DateTimeField(default=timezone.now() + timedelta(hours=24))

    def __str__(self):
        return self.title

class AvbMoney(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(default=0)


    def __str__(self):
        return f'Your balance is : {self.amount}'