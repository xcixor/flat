"""Contains room related views."""
from rest_framework import generics
from rest_framework import permissions
from flat.models import Room
from flat.serializers import RoomSerializer
from flat.permissions import IsOwnerOrReadOnly

class RoomList(generics.ListCreateAPIView):
    """
    List all room, or create a new room.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a room instance.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
