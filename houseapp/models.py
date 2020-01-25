from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    invite_code = models.CharField(max_length=6)
    members = models.ForeignKey(User, on_delete=models.CASCADE)

