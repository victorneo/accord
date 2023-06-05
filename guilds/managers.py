from django.db import models


class GuildEventManager(models.Manager):
    def publish_events(self):
        events = self.filter(published=False)
        for e in events:
            # 1. publish event to Discord
            # 2. Updated published to true
            # 3. Save object
            e.published = True
            e.save()