from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    # ex: /app/
    path('get_token/', views.get_csrf_token, name="get_csrf_token"),
]
