from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic
from .models import Gif, Video
from rest_framework import viewsets
from .serializer import VideoSerializer, GifSerializer


class IndexView(generic.ListView):
    template_name = 'video2gif/index.html'
    context_object_name = 'latest_video_list'

    # return Video.objects.filter()
    def get_queryset(self):
        return Video.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')


# rest api

#  video list get
class VideoList(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('create_time')
    serializer_class = VideoSerializer


# gif list get
class GifList(viewsets.ModelViewSet):
    queryset = Gif.objects.all().order_by('create_time')
    serializer_class = GifSerializer


