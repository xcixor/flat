from rest_framework import serializers
from django.contrib.auth.models import User
from flat.models import Room

class UserSerializer(serializers.HyperlinkedModelSerializer):
    rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'rooms']