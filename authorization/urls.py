from django.urls import include, path
from . import views

urlpatterns = [
    path("discord/callback", views.discord_callback, name="discord-callback"),
    path("", views.index, name="index"),
]
