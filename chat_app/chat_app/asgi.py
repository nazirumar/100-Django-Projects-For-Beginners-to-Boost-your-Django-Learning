
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import re_path

from api.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # Define your WebSocket routing here
            [
            re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi()),
            ]
        )
    ),
})
