from collections import defaultdict
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from course_reminders.models import Course, CourseReminder
from discord.guilds import send_message_to_channel


class Command(BaseCommand):
    def handle(self, **options):
        now = timezone.now()
        end = now + timedelta(days=7)

        courses = list(Course.objects.select_related('reminder_channel').all())
        template = courses[0].reminder_template
        channel_messages = defaultdict(lambda: template + '\n\n')

        reminder_ids = []

        for c in courses:
            qm = c.coursereminder_set.filter(published=False, start_time__range=(now, end)).order_by('start_time').all()

            reminders = list(qm)
            print(f'Total {len(reminders)} reminders for {c.name}')

            if len(reminders) == 0:
                continue

            reminders_msg = f'{c.name}\n'
            for r in reminders:
                reminder_ids.append(r.id)
                start_time = timezone.localtime(r.start_time).strftime('%m/%d %H:%M')
                end_time = timezone.localtime(r.end_time).strftime('%H:%M')
                reminders_msg += f'- {start_time} - {end_time} {r.message}\n'

            channel_messages[c.reminder_channel.discord_id] += reminders_msg + '\n'

        for discord_id, msg in channel_messages.items():
            send_message_to_channel(settings.DISCORD_BOT_TOKEN, discord_id, msg)

        print('Published all reminders')
        CourseReminder.objects.filter(id__in=reminder_ids).update(published=True)
