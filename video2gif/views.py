from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views import generic
from .models import Gif


class IndexView(generic.ListView):
    template_name = 'video2gif/index.html'
    context_object_name = 'latest_gif_list'

    # return Gif.objects.filter()
    def get_queryset(self):
        return Gif.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')
