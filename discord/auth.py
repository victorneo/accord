import requests

DISCORD_TOKEN_URL = 'https://discord.com/api/v10/oauth2/token'


class DiscordAccessToken(object):
    def __init__(self, access_token, refresh_token, guild_info):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.guild_info = guild_info


def get_access_token(client_id, client_secret, redirect_uri, code):
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code,
        'grant_type': 'authorization_code',
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    resp = requests.post(DISCORD_TOKEN_URL, data=data, headers=headers)

    return DiscordAccessToken(resp.json()['access_token'], resp.json()['refresh_token'], resp.json()['guild'])
