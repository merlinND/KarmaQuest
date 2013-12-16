from django.db import models
from django.contrib.auth.models import User as BaseUser

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Task(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    reward = models.PositiveIntegerField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

class Picture(models.Model):
    task = models.ForeignKey(Task)
    image = models.ImageField(upload_to='tasks/pictures')

class User(BaseUser):
    level = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    tasks = models.ManyToManyField(Task)
