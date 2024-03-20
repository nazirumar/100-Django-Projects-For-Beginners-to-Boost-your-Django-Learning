from django.urls import path
from api import views


urlpatterns = [
    path('chat/<slug:room_name>/messages/', views.MessageList.as_view(), name='chat-messages'),
]