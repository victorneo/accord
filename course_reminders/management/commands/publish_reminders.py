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

        courses = Course.objects.select_related('reminder_channel').all()

        for c in courses:
            qm = c.coursereminder_set.filter(published=False, start_time__range=(now, end)).order_by('start_time').all()

            reminders = list(qm)
            print(f'Total {len(reminders)} reminders for {c.name}')

            template = f'{c.reminder_template}\n\n'
            for r in reminders:
                start_time = r.start_time.strftime('%m/%d %H:%M')
                end_time = r.end_time.strftime('%H:%M')
                template += f'- {start_time} - {end_time} {r.message}\n'

            send_message_to_channel(settings.DISCORD_BOT_TOKEN, c.reminder_channel.discord_id, template)
            qm.update(published=True)
            print(f'Published reminders for {c.name}')
