from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ranking = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]