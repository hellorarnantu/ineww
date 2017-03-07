# coding=utf-8
from django.contrib import admin


from models import NewsModel


class NewsAdmin(admin.ModelAdmin):
    exclude = ('news_id', ),


admin.site.register(NewsModel, NewsAdmin)
