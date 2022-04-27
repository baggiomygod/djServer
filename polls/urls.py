from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote
    path('<int:question_id>/vote/', views.votes, name='vote'),
    # add question
    path('add_question/', views.add_question, name='add_question'),
    # add choice
    path('<int:question_id>/add_choice', views.add_choice, name='add_choice')
]
