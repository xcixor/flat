"""Room models serializers."""
from rest_framework import serializers
from flat.models.room_models.models import Room, ROOM_CHOICES


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    """Room instance serializer."""

    class Meta:
        model = Room
        fields = [
            'url', 'id', 'title', 'description',
            'location', 'price', 'room_type', 'owner', 'image'
            ]

    owner = serializers.ReadOnlyField(source='owner.username')
