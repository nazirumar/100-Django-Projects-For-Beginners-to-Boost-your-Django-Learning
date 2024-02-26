from django.urls import path
from chatapp import views

urlpatterns = [
    path('', views.chatgpt,  name='home')
]
