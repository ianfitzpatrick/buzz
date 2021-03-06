from django.db import models
from django.contrib.auth.models import User
from casters.models import Caster
from players.models import Player

class Stream(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    player = models.ForeignKey(
        Player, null=True, blank=True, related_name='streams',
        on_delete=models.SET_NULL
    )
    stream_id = models.CharField(max_length=255)
    max_viewer_count = models.SmallIntegerField(blank=True, default=0)
    thumbnail_url = models.CharField(max_length=255, blank=True, null=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    is_live = models.BooleanField(default=False)

    SERVICE_CHOICES = (
        ('TW', 'Twitch'),
        ('YT', 'Youtube'),
    )
    service = models.CharField(
        max_length=2, choices=SERVICE_CHOICES, default='TW')

    @property
    def link(self):
        if self.service == 'TW':
            return f'https://www.twitch.tv/{self.username}'
        elif self.service == 'YT':
            return f'https://www.youtube.com/watch?v={stream_id}'

        return ''

    @property
    def thumbnail(self):
        if self.thumbnail_url:
            if self.service == 'TW':
                return self.thumbnail_url.replace('{width}x{height}', '320x240')
            else:
                return self.thumbnail_url
        return ''
    
    def __str__(self):
        return f'{self.name}'

class StreamerBlacklist(models.Model):
    username = models.CharField(max_length=255)
    reason = models.CharField(max_length=255, blank=True, null=True)
