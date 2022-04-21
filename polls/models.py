from django.db import models


# Create your models here.

# models编辑完成运行以下两个命令:
# 1. py .\manage.py makemigrations polls
# 2. py .\manage.py sqlmigrate polls 0001
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    # ForeignKey告诉Django，每个Choice对象都关联到一个Question对象。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
