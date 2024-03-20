from rest_framework import serializers
from api.models import Room, Message


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'userslist')



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "room", "user", "content", "timestamp")
        read_only_fields = ("id", "timestamp")