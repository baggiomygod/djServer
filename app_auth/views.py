import json

from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render


# Create your views here.
def get_csrf_token(request):
    token = get_token(request)
    return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")
