from django.db import models
from users.models import User
from .managers import GuildEventManager


class Guild(models.Model):
    discord_id = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(null=False, max_length=200)
    users = models.ManyToManyField(User, related_name='guilds')


# Event id, name, when to add to Discord
class GuildEvent(models.Model):
    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3
    CHOICES = (
        (STAGE_INSTANCE, 'Stage Instance'),
        (VOICE, 'Voice'),
        (EXTERNAL, 'External'),
    )

    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel_id = models.TextField(null=True)

    name = models.TextField(null=False)

    publish_time = models.DateTimeField(null=False)
    published = models.BooleanField(default=False)

    scheduled_start_time = models.DateTimeField(null=False)
    scheduled_end_time = models.DateTimeField(null=False)

    event_type = models.IntegerField(
        null=False, choices=CHOICES, default=STAGE_INSTANCE)
    privacy_level = models.IntegerField(null=False, default=2)

    description = models.TextField(null=False)

    objects = GuildEventManager()