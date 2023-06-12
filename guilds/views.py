from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Guild, GuildChannel, ScheduledMessage


class ListGuildChannels(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        # Return all guild channels in this guild
        guild = get_object_or_404(Guild, discord_id=guild_id)
        channels = guild.guildchannel_set.all()

        serialized = [{'id': c.id, 'name': c.name, 'discord_id': c.discord_id, 'type': c.channel_type} for c in channels]
        return Response(serialized)


class ListScheduledMessages(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        # Return all scheduled messages in this guild
        guild = get_object_or_404(Guild, discord_id=guild_id)
        scheduled_messages = guild.scheduledmessage_set.select_related('channel').all()

        serialized = [{'channel': sm.channel.name,
                       'scheduled_time': sm.scheduled_time,
                       'published': sm.published,
                       'message': sm.message,}
                      for sm in scheduled_messages]
        return Response(serialized)


class ListChannelScheduledMessages(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, channel_id):
        channel = get_object_or_404(GuildChannel, id=channel_id)

        message = request.data.get('message')
        scheduled_time = request.data.get('scheduled_time')
        scheduled_time = datetime.strptime(scheduled_time, '%Y-%m-%dT%H:%M:%S.%f%z')

        sm = ScheduledMessage.objects.create(guild=channel.guild, channel=channel, message=message, scheduled_time=scheduled_time)

        return Response('success')
