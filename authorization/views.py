from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
import requests
from users.models import User
from guilds.models import Guild
from discord.auth import get_access_token
from discord.user import get_user_info


def discord_callback(request):
    '''
    Callback Params: discord/callback?code=&guild_id=&permissions=
    '''

    # Step 1: Get the code from the request
    code = request.GET.get("code")

    # Step 2: Exchange the code for tokens
    token = get_access_token(settings.DISCORD_CLIENT_ID, settings.DISCORD_CLIENT_SECRET, settings.DISCORD_REDIRECT_URI, code)

    # Step 3: Fetch user info from Discord
    user_info = get_user_info(token.access_token)

    # Step 4: Save user info in DB
    username = user_info.username + '#' + user_info.discriminator
    user, user_created = User.objects.get_or_create(
        discord_id=user_info.id,
        defaults={
            'username': username,
            'email': user_info.email,
            'discord_discriminator': user_info.discriminator,
            'discord_username': user_info.username,
        }
    )
    user.access_token = token.access_token
    user.refresh_token = token.refresh_token
    user.save()

    # Step 5: Create associated guild in DB
    guild, guild_created = Guild.objects.get_or_create(
        discord_id=token.guild_info['id'],
        defaults={
            'name': token.guild_info['name'],
        }
    )

    guild.users.add(user)

    return HttpResponse('You are {}, and are you a new account: {}. Guild {} is new: {}'.format(username, user_created, guild.discord_id, guild_created))
