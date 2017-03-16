# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '17-3-14'

from django.db import models
from django.contrib.auth.admin import User
from django.db.models import Q
import os
from utils.common_utils import get_uuid
from utils.time_utils import datetime_to_timestamp


class UserModel(models.Model):
    userId = models.CharField(default=get_uuid, max_length=32, primary_key=True, null=False, blank=False)  # 用户id
    user = models.ForeignKey(User, db_constraint=False, verbose_name=u'AUTH_USER')  #
    phone = models.CharField(max_length=20, default='', db_index=True, blank=True, verbose_name=u'手机号')
    username = models.CharField(max_length=50, default='', db_index=True, unique=True, verbose_name=u'用户昵称')
    gender = models.IntegerField(default=2, verbose_name=u'性别 0:男;1：女;2：未知')
    signature = models.CharField(max_length=100, default='', blank=True, verbose_name=u'个性签名')
    balance = models.DecimalField(default=0, verbose_name=u'余额', max_digits=10, decimal_places=2)
    avatar = models.CharField(default='', max_length=128, verbose_name=u'头像')
    mark = models.TextField(default='', blank=True, verbose_name=u'备注')

    is_delete = models.BooleanField(default=False, db_index=True, verbose_name=u'是否黑名单')  # 是否删除 false表示未删除
    qq_id = models.CharField(max_length=32, default='', db_index=True, blank=True, verbose_name=u'QQ号')
    wechat_id = models.CharField(max_length=32, default='', db_index=True, blank=True, verbose_name=u'微信号')
    weibo_id = models.CharField(max_length=32, default='', db_index=True, blank=True, verbose_name=u'微博号')
    role = models.IntegerField(default=0, verbose_name=u'角色')
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    updated_time = models.DateTimeField(auto_now=True)  # 更新时间

    def __unicode__(self):
        return self.username

    @property
    def avatar_url(self):
        return os.path.join("", self.avatar) if self.avatar else ''

    def list(self):
        return {
            'uid': self.userId,
            'phone': self.phone,
            'email': self.email,
            'username': self.username,
            'gender': self.gender,
            'created_time': datetime_to_timestamp(self.created_time),
        }

    def detail(self):
        return self.index().update(
            {"balance":self.balance}
        )

    def index(self):
        return {
            'uid': self.userId,
            'phone': self.phone,
            'email': self.email,
            'avatar': self.avatar_url,
            'username': self.username,
            'gender': self.gender,
            'signature': self.signature
        }

    class Meta:
        verbose_name_plural = u'用户管理'
        db_table = 'user'
        unique_together = ('phone', 'email')
        default_permissions = ()
        permissions = (
            ('delete', u'删除用户'),
            ('change', u'修改用户'),
            ('view', u'查看用户')
        )


class DoUserModel(object):

    @staticmethod
    def get_by_account(account):
        q = Q(phone=account)
        return UserModel.objects.filter(q).first()

    @staticmethod
    def get_by_id(uid):
        try:
            return UserModel.objects.get(userId=uid)
        except UserModel.DoesNotExist:
            return None