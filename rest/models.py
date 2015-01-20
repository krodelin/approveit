from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User)
    manager = models.ForeignKey(User, related_name='subordinates')


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    notes = models.TextField()

    def __str__(self):
        return self.title


class Request(models.Model):
    title = models.CharField(max_length=100, blank=False, default='')
    notes = models.TextField()
    project = models.ForeignKey(Project, related_name="requests")
    requester = models.ForeignKey(User, related_name='requester_requests')
    requestee = models.ForeignKey(User, related_name='requestee_requests')
