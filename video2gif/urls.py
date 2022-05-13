from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'videos', views.VideoList)
router.register(r'gifs', views.GifList)
app_name = 'video2gif'
urlpatterns = [
    # ex: /video2gif/
    path('', include(router.urls)),
    path('index', views.IndexView.as_view(), name='index'),
    path('upload', views.FileUploadView.as_view())
]
