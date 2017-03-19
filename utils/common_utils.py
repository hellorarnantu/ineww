# coding=utf-8
import json

import uuid
import re

PHONE_RE = "^1[3|4|5|8][0-9]\d{4,8}$"


def return_content(code, result=None, message=None):
    if result is None:
        result = {}
    code = code if isinstance(code, str) else str(code)
    return json.dumps(
        {
            # "message": message if message else HTTP_CODE[code],
            "code": code,
            "data": result
        },
        indent=4,
        ensure_ascii=False
    )


def get_uuid():
    return uuid.uuid4().hex


def valid_phone(phone_num):
    _match = re.match(PHONE_RE, phone_num)
    return True if _match else False

