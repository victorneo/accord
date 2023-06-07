from django.urls import include, path
from .views import ListGuildChannels


urlpatterns = [
    path("api/guilds/<str:guild_id>/channels", ListGuildChannels.as_view(), name="list-guild-channels"),
]
