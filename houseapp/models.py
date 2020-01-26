from datetime import date

from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse


class House(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    invite_code = models.CharField(max_length=6)
    members = models.ManyToManyField(User, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    date_joined = models.DateField()


class Task(models.Model):
    title = models.CharField(max_length=30)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


