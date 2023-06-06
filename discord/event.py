from datetime import datetime
import requests

DISCORD_SCHEDULED_EVENT_URL = 'https://discord.com/api/v10/guilds/{}/scheduled-events'


class DiscordUser(object):
    def __init__(self, id, username, discriminator, email):
        self.id = id
        self.username = username
        self.discriminator = discriminator
        self.email = email


def publish_event(bot_token, guild_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bot {}'.format(bot_token)}

    data = {
        'channel_id': None,
        'name': 'Test',
        'entity_metadata': {
            'location': 'https://google.com'
        },
        'privacy_level': 2,
        'scheduled_start_time': datetime.now().isoformat(),
        'description': 'hello',
        'entity_type': '3',
    }

    resp = requests.post(DISCORD_SCHEDULED_EVENT_URL.format(guild_id), data=data, headers=headers)
