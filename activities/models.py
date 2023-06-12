from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from guilds.models import ScheduledMessage


class ActivityType(models.Model):
    guild = models.ForeignKey('guilds.Guild', on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=200)
    reminder_weekly = models.BooleanField(default=False)
    reminder_same_day = models.BooleanField(default=False)

    reminder_weekly_channel = models.ForeignKey('guilds.GuildChannel', null=True, blank=True, on_delete=models.CASCADE, related_name='weekly_reminder_activity_types')
    reminder_same_day_channel = models.ForeignKey('guilds.GuildChannel', null=True, blank=True, on_delete=models.CASCADE, related_name='same_day_reminder_activity_types')

    def __str__(self):
        return f'{self.guild}: {self.name}'


class Activity(models.Model):
    guild = models.ForeignKey('guilds.Guild', on_delete=models.CASCADE)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=200)

    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    event_message = models.TextField(null=True, blank=True)

    scheduled_messages = models.ManyToManyField('guilds.ScheduledMessage', blank=True)

    def __str__(self):
        return f'{self.name} ({self.activity_type})'

    class Meta:
        verbose_name_plural = "activities"


@receiver(post_save, sender=Activity)
def create_profile(sender, activity, created, **kwargs):
    at = activity.activity_type

    if at.reminder_same_day and reminder_same_day_channel:
        scheduled_time = activity.start_time
        scheduled_time = scheduled_time.replace(hour=9, minute=0)

        sm = ScheduledMessage(guild=activity.guild,
                channel=at.reminder_same_day_channel,
                message=activity.event_message,
                scheduled_time=scheduled_time)
        sm.save()
