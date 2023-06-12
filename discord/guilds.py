import requests

DISCORD_GUILD_CHANNELS_URL = 'https://discord.com/api/v10/guilds/{}/channels'
DISCORD_GUILD_CREATE_MESSAGE_URL = 'https://discord.com/api/v10/channels/{}/messages'

DISCORD_CHANNEL_TYPES = {
    0: 'Text Channel',
    1: 'dm',
    2: 'Voice Channel',
    3: 'group_dm',
    4: 'category',
    5: 'announcement',
    10: 'announcement_thread',
    11: 'public_thread',
    12: 'private_thread',
    13: 'stage_voice',
    14: 'guild directory',
    15: 'guild forum',
}


class DiscordChannel(object):
    def __init__(self, discord_id, channel_type, name):
        self.discord_id = discord_id
        self.channel_type = channel_type
        self.name = name

    def __str__(self):
        return '{} [{}]'.format(self.name, DISCORD_CHANNEL_TYPES[self.channel_type])

    def __repr__(self):
        return self.__str__()

def get_guild_channels(bot_token, guild_id):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bot {}'.format(bot_token)}

    resp = requests.get(DISCORD_GUILD_CHANNELS_URL.format(guild_id), headers=headers)

    # for each channel in resp.json(), create a DiscordChannel object
    channels = [DiscordChannel(channel['id'], channel['type'], channel['name']) for channel in resp.json()]

    return channels


def send_message_to_channel(bot_token, channel_id, content):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bot {}'.format(bot_token)}

    data = {
        'tts': False,
        'content': content
    }

    resp = requests.post(DISCORD_GUILD_CREATE_MESSAGE_URL.format(channel_id), json=data, headers=headers)
