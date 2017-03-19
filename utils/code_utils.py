# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.cache import cache
from utils.constant import PHONE_CODE
import random


def send_code(phone):
    # code = "".join(random.sample("0123456789", 4))
    code = "1234"
    cache.set(PHONE_CODE["key"] % phone, code, PHONE_CODE["timeout"])
    return code

