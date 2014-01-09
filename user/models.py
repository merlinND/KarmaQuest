from django.db import models
from django.contrib.auth.models import User
from tasks.models import Task

class UserInformation(models.Model):
    user = models.ForeignKey(User)
    level = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    tasks = models.ManyToManyField(Task, blank=True)