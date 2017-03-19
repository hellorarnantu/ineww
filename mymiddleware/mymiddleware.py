# -*- coding: utf-8 -*-


from django.http import HttpResponse

from utils.common_utils import return_content
from session.models import DoAccessTokenModel


class MyAuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        token = request.META.get('HTTP_ACCESS_TOKEN', '')
        uid = request.META.get('HTTP_USER_ID', '')
        if request.path in ["/ineww/session", "/ineww/user", "/ineww/code/phone"] and request.method == 'POST':
            return self.get_response(request)

        if request.path in ["/ineww/user/phone"] and request.method == 'GET':
            return self.get_response(request)

        if not token or not uid:
            return HttpResponse(status=401, content=return_content("401001"))
        _token = DoAccessTokenModel.get_by_uid(uid)
        if not _token or _token.user_id != uid:
            return HttpResponse(status=401, content=return_content("401001"))
        request.uid = uid
        return self.get_response(request)
