import os
from django.core.exceptions import ValidationError
from rest_framework import serializers

from mysite import settings


# 校验文件后缀
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    size = value.size
    # valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    valid_extensions = ['.mp4']
    if not ext.lower() in valid_extensions:
        raise serializers.ValidationError('Unsupported file extension.', code='invalid ext')


# 校验文件大小
def file_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise serializers.ValidationError('File too large. Size should not exceed 5 MiB.', code='invalid size')
