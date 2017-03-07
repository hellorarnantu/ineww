# coding=utf-8

import time
import datetime

def datetime_to_timestamp(d):
    if not d:
        return ''
    mic = d.microsecond / 1000000.0
    d = d.strftime("%Y-%m-%d %H:%M:%S")
    t = time.mktime(time.strptime(d, '%Y-%m-%d %H:%M:%S'))
    return int(t + mic)


def timestamp_to_datetime(num, status=True):

    if status:
        num = float(num) / 1000
    return datetime.datetime.fromtimestamp(int(num))