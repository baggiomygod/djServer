from django.contrib import admin
from .models import Gif
from .models import Video


# Register your models here.

class GifAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Gif name', {'fields': ['name']}),
        ('Gif url', {'fields': ['url']}),
        ('Create time', {'fields': ['create_time']})
    ]
    date_hierarchy = 'create_time'
    list_display = ('id', 'name', 'url', 'create_time')
    list_filter = ['create_time']
    search_fields = ['name']
    list_per_page = 100


class GifInline(admin.TabularInline):
    model = Gif
    extra = 3


class VideoAmin(admin.ModelAdmin):
    fieldsets = [
        ('Video name', {'fields': ['name']}),
        ('Video url', {'fields': ['url']}),
        ('Video size', {'fields': ['size']}),
        ('Video type', {'fields': ['file_type']}),
        ('Create time', {'fields': ['create_time']}),
        ('User', {'fields': ['user_id']})
    ]
    date_hierarchy = 'create_time'
    list_display = ('id', 'name', 'url', 'size', 'file_type', 'create_time', 'user_id', 'user')
    list_filter = ['create_time', 'file_type']
    search_fields = ['name']
    list_per_page = 100


admin.site.register(Gif, GifAdmin)
admin.site.register(Video, VideoAmin)
