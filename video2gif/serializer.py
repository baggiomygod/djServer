# 序列化/反序列化json数据
from rest_framework import serializers
from .models import Video, Gif


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'size': {'required': False},
            'create_time': {'required': False},
            'file_type': {'required': False},
        }



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
