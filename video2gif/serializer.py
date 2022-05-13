# 序列化/反序列化json数据
from rest_framework import serializers
from .models import Video, Gif


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'name',
            'url',
            'size',
            'create_time'
        ]


class GifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gif
        fields = [
            'id',
            'name',
            'url',
            'create_time',
            'video_id'
        ]


# 文件上传服务 video
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
