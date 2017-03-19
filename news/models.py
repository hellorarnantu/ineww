# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from utils.time_utils import datetime_to_timestamp


class NewsModel(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, db_index=True)
    image = models.CharField(max_length=128, null=True, blank=True)
    author = models.CharField(max_length=32, null=True, blank=True)
    created_time = models.DateTimeField(null=True, blank=True)
    keywords = models.CharField(max_length=128, null=True, blank=True)
    original = models.CharField(max_length=128, null=True, blank=True)
    source = models.CharField(max_length=16, null=True, blank=True)
    content = models.TextField()
    reading_number = models.IntegerField(default=0)
    agree_number = models.IntegerField(default=0)
    disagree_number = models.IntegerField(default=0)
    category = models.IntegerField(default=0)
    brief = models.TextField(null=True, blank=True)
    md5 = models.CharField(max_length=32, null=True, db_index=True)

    def __unicode__(self):
        return self.title

    @property
    def created_timestamp(self):
        return datetime_to_timestamp(self.created_time)

    def info(self):
        return {
            "news_id": self.news_id,
            "title": self.title,
            "image": self.image,
            "author": self.author,
            "created_time": self.created_timestamp,
            "keywords": self.keywords,
            "source": self.source,
            "brief": self.brief,
            "category": self.category
        }

    def detail(self):
        info = self.info()
        info.update(
            {
                "original": self.original,
                "content": self.content
            }
        )
        return info

    class Meta:
        db_table = 'news'
        verbose_name_plural = u'新闻管理'
        default_permissions = ()
