from django.core.management.base import BaseCommand
from django.utils import timezone
from django.conf import settings
from guilds.models import ScheduledMessage
from discord.guilds import send_message_to_channel


class Command(BaseCommand):
    def handle(self, **options):
        now = timezone.now()

        qm = ScheduledMessage.objects.filter(published=False, scheduled_time__lte=now).select_related('channel')
        scheduled_messages = list(qm)

        num_messages = len(scheduled_messages)
        print(f'Total scheduled messages: {num_messages}')

        count = 0

        for sm in scheduled_messages:
            send_message_to_channel(settings.DISCORD_BOT_TOKEN, sm.channel.discord_id, sm.message)
            count += 1
            print(f'Published {count} out of {num_messages} messages')
