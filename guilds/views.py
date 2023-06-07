from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Guild


class ListGuildChannels(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        # Return all guild channels in this guild
        guild = get_object_or_404(Guild, discord_id=guild_id)
        channels = guild.guildchannel_set.all()

        serialized = [{'name': c.name, 'id': c.discord_id, 'type': c.channel_type} for c in channels]
        return Response(serialized)
