from django.contrib import admin
from .models import Guild, GuildChannel, ScheduledMessage, GuildEvent


class GuildAdmin(admin.ModelAdmin):
    pass

class GuildChannelAdmin(admin.ModelAdmin):
    pass

class ScheduledMessageAdmin(admin.ModelAdmin):
    list_display = ('guild', 'channel', 'published', 'message', 'scheduled_time')

class GuildEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(Guild, GuildAdmin)
admin.site.register(GuildChannel, GuildChannelAdmin)
admin.site.register(ScheduledMessage, ScheduledMessageAdmin)
admin.site.register(GuildEvent, GuildEventAdmin)
