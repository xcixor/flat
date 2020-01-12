from rest_framework import serializers
from django.contrib.auth.models import User
from flat.models import Room

class UserSerializer(serializers.ModelSerializer):
    rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'rooms']