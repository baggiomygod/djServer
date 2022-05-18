"""
Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看https://docs.djangoproject.com/zh-hans/4.0/topics/settings/ 了解细节。

Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6z-9-2db2nefv4_=isuqc&s6#db$z%mwe0!rsw)ca@#7@=lkbp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'app_auth.apps.AppAuthConfig',  # auth
    'upload.apps.UploadConfig',  # 上传
    'video2gif.apps.Video2GifConfig',  # 视频转GIF
    'polls.apps.PollsConfig',  # 投票
    'django.contrib.admin',  # 管理员站点
    'django.contrib.auth',  # 认证授权系统
    'django.contrib.contenttypes',  # 内容类型框架
    'django.contrib.sessions',  # 会话框架
    'django.contrib.messages',  # 消息框架
    'django.contrib.staticfiles',  # 管理静态文件的框架
    'rest_framework',  # restful api
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES':[
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ],
    # 全局配置异常模块
    'EXCEPTION_HANDLER': 'utils.exception.custom_exception_handler',
    # 修改默认返回JSON的renderer的类
    'DEFAULT_RENDERER_CLASSES': (
        'utils.rendererresponse.CustomerRenderer',
    ),
    # 访问权限
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',  # 普通用户
        # 'rest_framework.permissions.AllowAny', #所有用户
        # 'rest_framework.permissions.IsAdminUser',  # 管理员户
    ),
    # 身份认证的方式：jwt,session两种
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 前后端分离使用jwt验证
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # token验证 前端header头 {Authentication：Bearer token }, 为什么是Bearer？
        # 访问admin后台时使用
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# 覆盖JWT默认配置
SIMPLE_JWT = {
    # token有效时长
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    # token刷新后的有效时间
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
    # 'AUTH_HEADER_TYPES': ('JWT',)  # 请求头里的 前缀，这里覆盖默认的Bearer

}
# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"

# 后端测试登录成功后的重定向
LOGIN_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

"""
跨域和CSRF
"""
CSRF_TRUSTED_ORIGINS = ['http://localhost:9999', 'http://127.0.0.1:9999']
# SESSION_COOKIE_SECURE = True

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     '127.0.0.1:9999',
#     'loaclhost:9999'
# )
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    # postgresql
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'mydatabase',
    #     'USER': 'mydatabaseuser',
    #     'PASSWORD': 'mypassword',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fui_store',
        'USER': 'root',
        'PASSWORD': 'rbaggio10!',
        # 这里不要加'mysql://' 否则会报错 django.db.utils.OperationalError: (2059, ＜NULL>),
        # 网上有说是mysql密码加密方式问题，改了时候还是一样，后来去掉mysql:// 就好了
        'HOST': 'rm-bp1kqfk1r947048v79o.mysql.rds.aliyuncs.com',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False  # Flase 输出本地时间， True 输出UTC时间

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
