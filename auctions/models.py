from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=32, default="User")
    country = models.CharField(max_length=64, default="USA")

class Listing(models.Model):
    pass

class Bid(models.Model):
    pass

class Comment(models.Model):
    pass


