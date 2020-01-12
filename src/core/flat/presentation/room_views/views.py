"""Contains room related views."""
from rest_framework import generics
from flat.models import Room
from flat.serializers import RoomSerializer

class RoomList(generics.ListCreateAPIView):
    """
    List all room, or create a new room.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a room instance.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
