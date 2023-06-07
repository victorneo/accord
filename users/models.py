from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    discord_id = models.CharField(null=False, max_length=50, unique=True)
    discord_username = models.CharField(null=False, max_length=50)
    discord_discriminator = models.CharField(null=True, max_length=10)

    access_token = models.CharField(null=True, max_length=50)
    refresh_token = models.CharField(null=True, max_length=50)
    REQUIRED_FIELDS = ['discord_id', 'discord_username']
