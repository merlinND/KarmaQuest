from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Organization(models.Model):
    name = models.CharField(max_length=100)
    mission_statement = models.TextField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)

class Task(models.Model):
    organizer = models.ForeignKey(Organization)
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