from django.urls import path
from sesame.views import LoginView

urlpatterns = [

    path("login/auth/", LoginView.as_view(), name="login"),
 
]


