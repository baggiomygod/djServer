from django.db import models
from django.contrib.auth.models import User

# from utils.restrictedFileField import RestrictedFileField
from utils.FileFieldValidators import validate_file_extension, file_size


# Models 编辑完之后执行以下命令，翻译成数据库，并在数据库创建表
# python manage.py makemigrations video2gif
# py ./manage.py sqlmigrate polls 0001  执行迁移
# python manage.py migrate


class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    file_type = models.CharField(max_length=10)
    create_time = models.DateTimeField('video created')
    url = models.FileField(upload_to='djserver/upload/video', validators=[validate_file_extension, file_size])
    # url = RestrictedFileField(upload_to='djserver/upload/video',
    #                           content_types=['video/mp4'],
    #                           max_upload_size=settings.MAX_FILE_10M,
    #                           blank=True, null=True)


class Gif(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=100)
    url = models.ImageField(upload_to='djserver/upload/gif')
    create_time = models.DateTimeField('gif created')
