import requests

DISCORD_ME_URL = 'https://discord.com/api/v10/users/@me'


class DiscordUser(object):
    def __init__(self, id, username, discriminator, email):
        self.id = id
        self.username = username
        self.discriminator = discriminator
        self.email = email


def get_user_info(token) -> DiscordUser:
    headers = {'Authorization': 'Bearer {}'.format(token)}
    resp = requests.get(DISCORD_ME_URL, headers=headers)
    user_info = resp.json()
    return DiscordUser(user_info['id'], user_info['username'], user_info['discriminator'], user_info['email'])
