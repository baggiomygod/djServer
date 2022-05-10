from turtle import mode
from django.db import models


# Models 编辑完之后执行以下命令，翻译成数据库，并在数据库创建表
# python manage.py makemigrations video2gif
# py ./manage.py sqlmigrate polls 0001  执行迁移
# python manage.py migrate


class Video(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    type = models.CharField(max_length=10)
    url = models.FileField(upload_to='djserver/upload/video')
    create_time = models.DateTimeField('video created')


class Gif(models.Model):
    video = models.ForeignKey(Video, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100)
    url = models.ImageField(upload_to='djserver/upload/gif')
    create_time = models.DateTimeField('gif created')
