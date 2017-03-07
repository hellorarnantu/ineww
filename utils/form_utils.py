#coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

import json
from django.http import HttpResponse, HttpResponseBadRequest
from functools import wraps
from .common_utils import return_content

# form验证
def validate_form(form_class, data):
    form = form_class(data)
    if form.is_valid():
        return True, form.cleaned_data
    errors = []
    for key, field in form.declared_fields.items():
        if field.required and key not in data:
            errors.append({"field": key, "code": "missing_field"})
        elif key in form.errors:
            errors.append({"field": key, "code": "invalid"})
    return False, errors


def dec_validate_form(form_class):
    def _dec(fun):
        @wraps(fun)
        def wrapper(view, request, *args, **kwargs):
            method = request.method
            if request.method in ['PUT', 'POST']:
                try:
                    setattr(request, method, json.loads(request.body if request.body else '{}'))
                    # request.PUT = json.loads(request.body if request.body else '{}')
                except ValueError:
                    return HttpResponseBadRequest(return_content(code='400010'))

            data = getattr(request, request.method)
            # if not data:
            #     return HttpResponse(status=422, content=return_content(code='422001', result=data))
            # print data
            flag, data = validate_form(form_class, data)
            if not flag:
                return HttpResponse(status=422, content=return_content(code='422001', result=data))
            request.data = data
            return fun(view, request, *args, **kwargs)

        return wrapper

    return _dec