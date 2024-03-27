from django.contrib import admin
from .models import Gif
from .models import Video


# Register your models here.

class GifAddmin(admin.ModelAdmin):
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


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Video name', {'fields': ['name']}),
        ('Video url', {'fields': ['url']}),
        ('Video size', {'fields': ['size']}),
        ('Video type', {'fields': ['file_type']}),
        ('Create time', {'fields': ['create_time']}),
        ('User', {'fields': ['user']}) # 在models.py中，有Video与User模型关联的字段，在Video.Admin中就不该使用user_id, 而是user
        # 正确的方式应该是如上 
        # 引入user_id会导致报错： Unknown field(s) (user_id) specified for Video. Check fields/fieldsets/exclude attributes of class VideoAmin
        # ('User', {'fields': ['user_id']}) # 会导致报错！！！
    ]
    date_hierarchy = 'create_time'
    list_display = ('id', 'name', 'url', 'size', 'file_type', 'create_time', 'user_id', 'user')
    list_filter = ['create_time', 'file_type']
    search_fields = ['name']
    list_per_page = 100


admin.site.register(Gif, GifAddmin)
admin.site.register(Video, VideoAdmin)
