import os
import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gif, Video
from rest_framework import viewsets, status
from .serializer import VideoSerializer, GifSerializer


class IndexView(generic.ListView):
    template_name = 'video2gif/index.html'
    context_object_name = 'latest_video_list'

    # return Video.objects.filter()
    def get_queryset(self):
        return Video.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')


"""
# rest api
"""


#  video list get
class VideoList(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('create_time')
    serializer_class = VideoSerializer
    # parser_classes = [FileUploadParser]


# 上传视频
class VideoAdd(CreateAPIView):
    # MultiPartParser: multipart/form-data
    # FormParser: application/x-www-form-urlencoded
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    serializer_class = VideoSerializer

    def post(self, request, *args, **kwargs):
        # 将文件大小和类型及时间添加到参数
        file = request.data.get('url')
        ext = os.path.splitext(file.name)[1]
        data = request.data
        data['file_type'] = ext
        data['size'] = file.size
        data['create_time'] = timezone.now()
        data['user'] = request.user.id
        serializer = VideoSerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()  # 上传并在数据库记录
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# gif list get
class GifList(viewsets.ModelViewSet):
    queryset = Gif.objects.all().order_by('create_time')
    serializer_class = GifSerializer


# 上传图片
class GifAdd(CreateAPIView):
    # MultiPartParser: multipart/form-data
    # FormParser: application/x-www-form-urlencoded
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, *args, **kwargs):
        # 将文件大小和类型及时间添加到参数
        data = request.data
        data['create_time'] = timezone.now()
        data['user'] = request.user.id
        serializer = GifSerializer(data=data)
        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()  # 上传并在数据库记录
            return Response(serializer.data, status=status.HTTP_201_CREATED)
