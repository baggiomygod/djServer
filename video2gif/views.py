from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gif, Video
from rest_framework import viewsets, status
from .serializer import VideoSerializer, GifSerializer, FileSerializer


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


# 上传接口
class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
