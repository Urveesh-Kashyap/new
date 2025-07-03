from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class user_data(AbstractUser):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)