# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from .models import AccessTokenModel


def log_out(uid):
    AccessTokenModel.objects.filter(user_id=uid).delete()
