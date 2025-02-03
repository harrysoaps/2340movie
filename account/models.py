import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib import admin


class account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.username, self.password
