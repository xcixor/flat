"""Room models serializers."""
from rest_framework import serializers
from flat.models.room_models.models import Room, ROOM_CHOICES


class RoomSerializer(serializers.ModelSerializer):
    """Room instance serializer."""

    class Meta:
        model = Room
        fields = ['id', 'title', 'description', 'location', 'price', 'room_type']