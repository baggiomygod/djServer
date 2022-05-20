# 序列化/反序列化json数据
import os
from rest_framework import serializers
from .models import Video, Gif


class VideoSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username", read_only=True)

    class Meta:
        model = Video
        # fields 每一个Form类的字段不仅负责验证数据，同样需要“清理”数据 — 标准化为统一的格式。
        # 序列化字段负责在原始数据和内部数据类型之间转换。它们同样负责校验输入的值，以及从父级对象查询和设置值。
        # 如果这里的字段与SomeSerializer(data={'user':'1'}), data中的key不对应会为Null, data.user_id，则无法保存user_id, 需要是'user'
        fields = [
            'id',
            'name',
            'url',
            'size',
            'create_time',
            'file_type',
            'user',
            'username'
        ]
        # fields = '__all__'

        extra_kwargs = {
            'name': {'required': True},
            'size': {'required': True},
            'create_time': {'required': True},
            'file_type': {'required': True},
        }


class GifSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username", read_only=True)

    class Meta:
        model = Gif
        fields = [
            'id',
            'name',
            'url',
            'create_time',
            'user',
            'username'
        ]
