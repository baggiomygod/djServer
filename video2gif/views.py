import os

from django.contrib.auth.models import User
# Create your views here.
from django.utils import timezone
from django.views import generic
from moviepy.editor import *
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from mysite.settings import FILE_VIDEO_DIR
from .models import Gif, Video
from rest_framework import viewsets, status
from .serializer import VideoSerializer, GifSerializer


class IndexView(generic.ListView):
    """首页"""
    template_name = 'video2gif/index.html'
    context_object_name = 'latest_video_list'

    # return Video.objects.filter()
    def get_queryset(self):
        return Video.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')


#  video list get
class VideoView(viewsets.ModelViewSet):
    """视频"""
    perms_map = {
        'get': '*',
        'post': 'video_create',
        'put': 'video_update',
        'delete': 'video_delete'
    }
    queryset = Video.objects.all().order_by('create_time')
    serializer_class = VideoSerializer
    pagination_class = None
    search_fields = ['name']
    ordering_fields = ['create_time']
    ordering = ['create_time']

    # /video2gif/videos/add
    @action(methods=['post'], detail=False)
    def add(self, request):
        """新增"""
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

    # /video2gif/videos/{id}/convert_to_gif
    @action(methods=['post'], detail=True)
    @parser_classes([JSONParser])
    def convert_to_gif(self, request, *args, **kwargs):
        """
            转换
            params:
            {
                start?, end?, resize?
            }
        """
        data = request.data
        print('args:', args)
        print('data:', data)
        print('kwargs pk:', kwargs['pk'])
        video = Video.objects.get(pk=kwargs['pk'])
        serializer = VideoSerializer(instance=video)
        url = serializer.data['url']
        v_path = os.path.join(FILE_VIDEO_DIR, os.path.basename(url))
        g_path = v_path.replace('.mp4', '.gif')
        size = data.get('size') or 1
        start = data.get('start') or 0
        end = data.get('end') or None
        clip = VideoFileClip(v_path).resize(size)
        # getting only first 3 seconds
        clip = clip.subclip(start, end)

        # saving video clip as gif
        clip.write_gif(g_path, fps=40)

        # loading  gif
        gif = VideoFileClip(g_path)

        new_gif_url = url.replace('.mp4', '.gif')
        # 获取数据库，检查是否已存在
        gif_existed = Gif.objects.filter(url=new_gif_url)
        save_data = {
            "user_id": request.user.id,
            "create_time": timezone.now(),
            "name": os.path.basename(g_path),
            "url": new_gif_url
        }
        # 如果已存在更新，否则插入新的数据
        if gif_existed:
            gif_existed.update(**save_data)
            return Response({"id": gif_existed[0].id, "name": gif_existed[0].name}, status=status.HTTP_201_CREATED)
        else:
            gif_save = Gif.objects.create(**save_data)
        return Response({"id": gif_save.id, "name": gif_save.name}, status=status.HTTP_201_CREATED)


class GifView(viewsets.ModelViewSet):
    """GIF"""
    queryset = Gif.objects.all().order_by('create_time')
    serializer_class = GifSerializer

    # 上传图片
    @action(methods=['post'], detail=False)
    def add(self, request):
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
