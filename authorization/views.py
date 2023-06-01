from django.conf import settings
import requests
from django.shortcuts import render
from django.http import HttpResponse

DISCORD_TOKEN_URL = 'https://discord.com/api/v10/oauth2/token'
DISCORD_ME_URL = 'https://discord.com/api/v10/oauth2/@me'

def discord_callback(request):
    '''
    Callback Params: discord/callback?code=&guild_id=&permissions=
    '''

    # Step 1: Get the code from the request
    code = request.GET.get("code")

    # Step 2: Exchange the code for tokens
    data = {
        'client_id': settings.DISCORD_CLIENT_ID,
        'client_secret': settings.DISCORD_CLIENT_SECRET,
        'redirect_uri': settings.DISCORD_REDIRECT_URI,
        'code': code,
        'grant_type': 'authorization_code',
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp = requests.post(DISCORD_TOKEN_URL, data=data, headers=headers)
    access_token = resp.json()['access_token']
    refresh_token = resp.json()['refresh_token']

    # Step 3: Fetch user info from Discord
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    resp = requests.get(DISCORD_ME_URL, headers=headers)

    return HttpResponse('You are {}'.format(resp.json()['user']['username']))