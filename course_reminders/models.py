from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from guilds.models import ScheduledMessage


class Course(models.Model):
    guild = models.ForeignKey('guilds.Guild', on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=200)
    reminder_template = models.TextField()
    reminder_channel = models.ForeignKey('guilds.GuildChannel', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guild}: Course {self.name}'


class CourseReminder(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    message = models.CharField(null=False, max_length=200)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course} ({self.message})'
