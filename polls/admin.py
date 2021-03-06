from django.contrib import admin
from .models import Question, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 修改顺序
    fieldsets = [
        ('Question information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    date_hierarchy = 'pub_date'  # 日期层次结构
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # table 列
    list_filter = ['pub_date']  # 过滤条件
    search_fields = ['question_text']  # 搜索框
    list_per_page = 100  # 每页条数
    inlines = [ChoiceInline]


class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('choice_text information', {'fields': ['choice_text']}),
        ('votes information', {'fields': ['votes'], 'classes': ['collapse']}),
    ]
    list_display = ('choice_text', 'votes', 'question_id', 'question')  # table 列
    search_fields = ['choice_text']  # 搜索框
    list_per_page = 100  # 每页条数


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
