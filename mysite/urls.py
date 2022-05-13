"""mysite URL Configuration
Django 项目的 URL 声明，就像你网站的“目录”。阅读 URL调度器 文档来获取更多关于 URL 的内容。
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

# from rest_framework.routers import DefaultRouter
# from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # 测试登录
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # drf自带的token授权登录，获取token需要向该地址post数据
    path('api-token-auth/', views.obtain_auth_token),

    # jwt的token认证
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 验证Token的有效性
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('app/', include('app_auth.urls')),
    path('video2gif/', include('video2gif.urls')),
]
