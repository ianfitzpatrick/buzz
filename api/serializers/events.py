from rest_framework import serializers
from events.models import Event, EventLink
from .players_nested import PlayerSerializerSummary

class EventLinkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EventLink
        fields = ['name', 'url']


class EventSerializer(serializers.ModelSerializer):
    links = EventLinkSerializer(many=True)
    organizers = PlayerSerializerSummary(many=True)
    
    class Meta:
        model = Event
        fields = [
            'name', 'start_time', 'duration', 'description', 'organizers',
            'links', 'created', 'modified'
        ]
