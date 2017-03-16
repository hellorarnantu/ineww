# -*- coding: utf-8 -*-


from django.http import HttpResponse

from users.models import DoUserModel
from django.contrib.auth.tokens import default_token_generator
from utils.common_utils import return_content


class QtsAuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        token = request.META.get('HTTP_ACCESS_TOKEN', '')
        uid = request.META.get('HTTP_USER_ID', '')
        if not token or not uid:
            return HttpResponse(status=401, content=return_content("401001"))
        user = DoUserModel.get_by_id(uid)
        if user:
            access_token = default_token_generator(user.user)
            if access_token != token:
                return HttpResponse(status=401, content=return_content("401001"))

            request.uid = user.uid
            request.user= user

            return  self.get_response(request)
        return HttpResponse(status=401, content=return_content("401001"))

