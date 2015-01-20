from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User)
    manager = models.ForeignKey(User, related_name="subordinates")