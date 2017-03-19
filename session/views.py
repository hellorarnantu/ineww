# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from django.http import HttpResponse
from .forms import SessionForm
from utils.form_utils import dec_validate_form
from users.models import DoUserModel
from django.contrib.auth import login
from utils.common_utils import return_content
from .models import DoAccessTokenModel
from session.helper import log_out


class SessionView(View):
    @dec_validate_form(SessionForm)
    def post(self, request):
        account = request.param["account"]
        password = request.param["password"]

        user = DoUserModel.get_by_account(account)
        if not user:
            return HttpResponse(status=401, content=return_content("401003"))

        if not user.user.is_active:
            return HttpResponse(status=401, content=return_content("401002"))
        if not user.user.check_password(password):
            return HttpResponse(status=401, content=return_content("401003"))
        login(request, user.user)
        token, _ = DoAccessTokenModel.generate_token(user.userId)
        return HttpResponse(return_content("200001", {
            "token": token.detail(),
            "user": user.detail()
        }))

    def get(self, request):
        user = DoUserModel.get_by_id(request.uid)
        return HttpResponse(return_content("200001", user.detail()))

    def delete(self, request):
        log_out(request.uid)
        return HttpResponse(status=204, content=return_content("204001"))
