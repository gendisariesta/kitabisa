from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  name = models.CharField(max_length=250)
  location = models.CharField(max_length=50, null=True)

  def __str__(self):
    return "{}".format(self.name)