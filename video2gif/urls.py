from django.urls import path, include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()

# 'r'是防止字符转义的
router.register(r'videos', views.VideoList)
router.register(r'gifs', views.GifList)
# router.register(r'video_add', views.VideoAdd)


app_name = 'video2gif'
urlpatterns = [
    # ex: /video2gif/
    path('', include(router.urls)),
    path('index', views.IndexView.as_view(), name='index'),
    path('video_add/', views.VideoAdd.as_view(), name='video_add'),
    path('gif_add/', views.GifAdd.as_view(), name='gif_add'),
    path('video2gif/', views.Video2Gif.as_view(), name="video_gif")
]


