# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from .models import UserModel, DoUserModel
from session.models import DoAccessTokenModel
from utils.form_utils import dec_validate_form
from .forms import UserSaveForm, UserUpdateForm, PwdForm, AccountForm, PhoneForm
from utils.common_utils import return_content
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.core.cache import cache
from utils.constant import PHONE_CODE
from django.db import transaction

from session.helper import log_out


class UsersView(View):
    # 注册

    @transaction.atomic
    @dec_validate_form(UserSaveForm)
    def post(self, request):
        pwd = request.param["pwd"]
        phone = request.param["phone"]
        code = request.param["code"]
        if cache.get(PHONE_CODE['key'] % phone, "") != code:
            return HttpResponseBadRequest(return_content("400004"))  # 验证码错误
        if DoUserModel.is_exist_by_phone(phone):
            return HttpResponseBadRequest(return_content("400003"))  # 手机号重复
        del request.param["pwd"]
        del request.param["agree"]
        del request.param["code"]
        user = User(username=request.param["phone"])
        user.set_password(pwd)
        user.save()
        obj = UserModel.objects.create(user=user, **request.param)
        token, _ = DoAccessTokenModel.generate_token(obj.userId)

        return HttpResponse(return_content("201001", {
            "token": token.detail(),
            "user": obj.detail()
        }))


class UserView(View):
    # 修改
    @dec_validate_form(UserUpdateForm)
    def put(self, request, user_id):
        if user_id != request.uid:
            return HttpResponseForbidden(return_content("403001"))
        user = DoUserModel.get_by_id(user_id)
        for k, v in request.param.items():
            setattr(user, k, v)
        user.save(update_fields=request.param.keys())
        return HttpResponse(status=204)

    # 获取
    def get(self, request, user_id):
        if request.uid == user_id:
            user = UserModel.objects.get(userId=user_id)
            if user:
                return HttpResponse(return_content("200001", user.detail()))
            return HttpResponseNotFound(return_content("404001"))
        return HttpResponseForbidden(return_content("403001"))


class AccountView(View):
    @dec_validate_form(AccountForm)
    def put(self, request):
        phone = request.param["phone"]
        user = DoUserModel.get_by_id(uid=request.uid)

        if DoUserModel.is_exist_by_phone(phone):
            return HttpResponseBadRequest(return_content("400003"))  # 手机号重复

        if cache.get(PHONE_CODE['key'] % phone, "") != request.param["code"]:
            return HttpResponseBadRequest(return_content("400004"))  # 验证码错误
        # print connection.queries
        user.phone = phone
        user.save(update_fields=["phone"])
        user.user.username = phone
        user.user.save(update_fields=["username"])
        return HttpResponse(status=204, content=return_content("204001"))

    @dec_validate_form(PhoneForm)
    def get(self, request):
        flag = DoUserModel.is_exist_by_phone(request.param["phone"])
        return HttpResponse(return_content("200001", {"is_exist": flag}))


class PwdView(View):
    @dec_validate_form(PwdForm)
    def put(self, request):
        user = DoUserModel.get_by_id(request.uid)
        if not user.user.check_password(request.param["re_pwd"]):
            return HttpResponse(status=401, content=return_content("401003"))
        user.user.set_password(request.param["pwd"])
        user.user.save()
        log_out(request.uid)
        return HttpResponse(status=204, content=return_content("204001"))


# 获取用户主页
class IndexUserView(View):
    def get(self, request, user_id):
        user = UserModel.objects.get(userId=user_id)
        if user:
            return HttpResponse(return_content("200001", user.index()))
        return HttpResponseNotFound(return_content("404001"))
