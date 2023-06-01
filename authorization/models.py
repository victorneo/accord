from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    discord_id = models.TextField(null=False, unique=True)
    discord_username = models.TextField(null=False)
    discord_discriminator = models.TextField(null=True)
    REQUIRED_FIELDS = ['discord_id', 'discord_username']