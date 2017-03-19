# coding=utf-8

from django.db import models
from django.contrib.auth.admin import User
from django.db.models import Q
import os
from utils.common_utils import get_uuid
from utils.time_utils import datetime_to_timestamp, timestamp_to_datetime
from users.models import UserModel
import time
from ineww.settings import ACCESS_TOKEN_EXPIRES
from ineww.settings import REFRESH_TOKEN_EXPIRES
import uuid


class AccessTokenModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserModel, db_constraint=False)
    access_token = models.CharField(max_length=128)
    refresh_token = models.CharField(max_length=128)
    access_token_expired = models.DateTimeField()
    refresh_token_expired = models.DateTimeField()

    @property
    def access_token_expired_timestamp(self):
        return datetime_to_timestamp(self.access_token_expired)

    @property
    def refresh_token_expired_timestamp(self):
        return datetime_to_timestamp(self.refresh_token_expired)

    class Meta:
        db_table = 'access_token'
        default_permissions = ()

    def detail(self):
        return {
            "access_token_expired": self.access_token_expired_timestamp,
            "refresh_token_expired": self.refresh_token_expired_timestamp,
            "access_token": self.access_token,
            "refresh_token": self.refresh_token
        }


class DoAccessTokenModel(object):
    @staticmethod
    def generate_token(user_id):
        access_token_expire = int(time.time() + ACCESS_TOKEN_EXPIRES)
        refresh_token_expire = int(time.time() + REFRESH_TOKEN_EXPIRES)
        access_token_expired = timestamp_to_datetime(access_token_expire, False)
        refresh_token_expired = timestamp_to_datetime(refresh_token_expire, False)
        access_token = uuid.uuid4().hex
        refresh_token = uuid.uuid4().hex
        print access_token_expired
        return AccessTokenModel.objects.update_or_create(user_id=user_id,
                                                      defaults=dict(access_token=access_token,
                                                                    refresh_token=refresh_token,
                                                                    access_token_expired=access_token_expired,
                                                                    refresh_token_expired=refresh_token_expired))

    @staticmethod
    def get_by_uid(uid):
        return AccessTokenModel.objects.filter(user_id=uid).first()
