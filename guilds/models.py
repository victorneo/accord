from django.db import models


class Guild(models.Model):
    discord_id = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(null=False, max_length=200)
    users = models.ManyToManyField('authorization.User', related_name='guilds')