from django.urls import path
from django.contrib.auth import views as log_views
from accounts import views
urlpatterns = [
    path('', views.home,name='home'),
    path('login',  log_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout',  log_views.LogoutView.as_view(), name='logout'),
]
