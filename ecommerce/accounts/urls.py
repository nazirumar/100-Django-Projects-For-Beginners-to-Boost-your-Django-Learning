from django.contrib.auth import views as log_views
from django.urls import path
from django.conf import settings

from accounts import views

app_name = 'account'

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', log_views.LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
]

