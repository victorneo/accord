from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from guilds.models import Guild
from .models import Activity, ActivityType


class ListActivityTypes(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        guild = get_object_or_404(Guild, id=guild_id)
        atypes = ActivityType.objects.filter(guild=guild).all()

        serialized = [{'name': a.name, 'reminder_weekly': a.reminder_weekly,
                       'reminder_same_day': a.reminder_same_day} for a in atypes]

        return Response(serialized)


class ListActivities(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, guild_id):
        guild = get_object_or_404(Guild, id=guild_id)
        activities = Activity.objects.filter(guild=guild).select_related('activity_type').all()

        serialized = [{'name': a.name, 'activity_type': a.activity_type.name,
                       'start_time': a.start_time, 'end_time': a.end_time,
                       'event_message': a.event_message} for a in activities]

        return Response(serialized)

    def post(self, request, guild_id):
        guild = get_object_or_404(Guild, id=guild_id)
        return Response({})
