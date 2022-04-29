from django.contrib import admin
from .models import Gif


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


admin.site.register(Gif, GifAdmin)
