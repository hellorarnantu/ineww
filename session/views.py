# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '17-3-14'

from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from django.http import HttpResponse, HttpResponseForbidden
from .forms import SessionForm
from utils.form_utils import dec_validate_form
from users.models import UserModel, DoUserModel
from django.contrib.auth import login, logout
from django.contrib.auth.tokens import default_token_generator
from utils.common_utils import return_content

class SessionView(View):
    @dec_validate_form(SessionForm)
    def post(self, request):
        account = request.param["account"]
        password = request.param["password"]

        user = DoUserModel.get_by_account(account)
        if not user.user.is_active:
             return HttpResponse(status=401,content=return_content("401002"))
        if not user.user.check_password(password):
            return HttpResponse(status=401, content=return_content("401003"))
        login(request, user.user)
        access_token = default_token_generator.make_token(user.user)
        return HttpResponse(return_content("200001", {
            "user":user.detail(),
            "access_token":access_token,
        }))



    def post(self, request):
        return HttpResponse(return_content("200001", ))


    def delete(self, request):
        login(request, request.user.user)
        return HttpResponse(status=204,content=return_content("204001"))

