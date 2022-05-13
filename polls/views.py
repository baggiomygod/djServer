from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Question, Choice
from django.utils import timezone
import random
from django.template import loader
from django.shortcuts import render, get_object_or_404


# 原列表
# (context)。这个上下文是一个字典，它将模板内的变量映射为 Python 对象。
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # 对应index.html里的latest_question_list
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


# 通用视图替代index
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # pub_date__lte='2020-01-01'相当于
        # SELECT * FROM blog_entry WHERE pub_date <= '2020-01-01';
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]


def add_question(request):
    q = Question(question_text="what's up? %d." % random.randint(0, 999), pub_date=timezone.now())
    q.save()
    return HttpResponse('success')


# 原详情
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# 通用视图代替detail
class DetailView(generic.DetailView):
    model = Question
    # template_name属性是用来告诉Django使用一个指定的模板名字
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet
        """
        # pub_date小于当前时间，即过去时间
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def add_choice(request, question_id):
    q = get_object_or_404(Question, pk='2')
    c = q.choice_set.create(choice_text="选项 %d." % random.randint(0, 999), votes=0)
    return HttpResponse('success')


def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
        print('choice:', select_choice.choice_text, select_choice.id)
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice!!!"
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
