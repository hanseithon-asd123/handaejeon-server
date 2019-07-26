from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='blog/%Y/%m/%d')
    ranking = models.IntegerField(blank=False, null=False)
    point = models.IntegerField(blank=False, null=False)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]