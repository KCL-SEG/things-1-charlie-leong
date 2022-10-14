from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.db.models import Model

class User(AbstractUser):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
