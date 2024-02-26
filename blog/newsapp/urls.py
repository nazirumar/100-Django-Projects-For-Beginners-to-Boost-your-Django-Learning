from django.urls import path
from newsapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('new-post', views.create_post, name='new-post'),
    path('blog/<str:pk>', views.blog_detail, name='blog'),
    path('liked/<str:pk>', views.liked, name='liked')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)