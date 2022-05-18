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
            'type',
            'size',
            'create_time'
        ]
        extra_kwargs = {
            'name': {'required': True},
            'size': {'required': False},
            'create_time': {'required': False},
            'type': {'required': False},
        }

    def create(self, validated_data):
        obj = Video.objects.create(
            url=self.context['request'].data.get('url', None)
        )
        return obj


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
