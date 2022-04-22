import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

# models编辑完成运行以下两个命令:
# 1. py ./manage.py makemigrations polls  根据对models（模型）的改变，创建迁移文件
# 2. py ./manage.py sqlmigrate polls 0001  执行迁移
# 3. py ./manage.py migrate 应用数据库迁移， 在数据库中创建响应的表
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_publish_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # ForeignKey告诉Django，一个Question对多个Choice
    # on_delete = models.CASCADE： 删除关联数据1端,与之关联也（多端）删除
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
