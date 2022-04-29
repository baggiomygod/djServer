from django.urls import path
from . import views

app_name = 'video2gif'
urlpatterns = [
    # ex: /video2gif/
    path('', views.IndexView.as_view(), name='index'),
]
