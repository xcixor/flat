"""Room filters."""
from rest_framework import filters
from rest_framework import generics
from django.contrib.auth.models import User
from flat.models import Room
from flat.serializers import RoomSerializer


class UserRoomList(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):

        """
        Optionally restricts the returned rooms to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Room.objects.all()
        user_name = self.request.query_params.get('username', None)
        if user_name is not None:
            user = User.objects.filter(username=user_name).first()
            queryset = queryset.filter(owner=user)
        return queryset


class RoomList(generics.ListAPIView):
    """
    Optionally restrict the returned list of rooms by filtering against
    `location`, `room_type`, `price` and `owner`
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filterset_fields = ['location', 'room_type', 'owner']


class MultipleFieldsQueryListView(generics.ListAPIView):
    """
    Search in all fields for the occurece of a `search` paramater
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'room_type', 'price', 'owner__id', 'description', 'title']