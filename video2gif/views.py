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
    
class VideoAdd1(CreateAPIView):
    parser_classes = (MultiPartParser, FormParser, )
    serializer_class = VideoSerializer

# class VideoAdd2(CreateAPIView):
#     # MultiPartParser: multipart/form-data
#     # FormParser: application/x-www-form-urlencoded
#     parser_classes = (MultiPartParser, FormParser, )
#     serializer_class = VideoSerializer

#     def post(self, request, *args, **kwargs):
#         print('VideoAdd content_type:', request.content_type)
#         print('VideoAdd data:', request.data)
#         print('VideoAdd FILES:', request.FILES)
#         serializer = self.serializer_class(data=request.data)
#         # serializer = self.serializer_class(data=request.data)
#         if not serializer.is_valid():
#             return Response({'message': str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             url = request.FILES
#             print('url:', url)
#             name = serializer.data.get('name')
#             type_val = serializer.data.get('type')
#             create_time = serializer.data.get('create_time')
#             size = serializer.data.get('size')
#             video = Video(url=url, name=name, type=type_val, create_time=create_time, size=size)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print('errors:', serializer.errors)
#         return Response({'message': 'creat filed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# gif list get
class GifList(viewsets.ModelViewSet):
    queryset = Gif.objects.all().order_by('create_time')
    serializer_class = GifSerializer
