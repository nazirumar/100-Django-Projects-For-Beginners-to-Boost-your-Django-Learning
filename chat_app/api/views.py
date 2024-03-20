


from rest_framework import generics

from api.serializers import MessageSerializer
from api.models import Message

class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    ordering = ('-timestamp',)
    
    def get_queryset(self):
        room_name = self.kwargs.get('room_name')
        if room_name:
            queryset = Message.objects.filter(room__name=room_name)
        else:
            queryset = Message.objects.all()
        return queryset