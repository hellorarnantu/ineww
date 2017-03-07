# coding=utf-8
import json

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