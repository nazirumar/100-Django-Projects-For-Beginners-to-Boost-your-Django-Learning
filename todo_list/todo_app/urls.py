from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<str:pk>/', views.upadateView, name='update'),
    path('delete/<str:pk>/', views.deleteView, name='delete'),
    path('detail/<str:pk>/', views.detailview, name='detail'),
]