# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from .models import UserModel
from utils.form_utils import dec_validate_form
from .forms import UserSaveForm
from utils.common_utils import return_content
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden


class UsersView(View):
    # 注册
    @dec_validate_form(UserSaveForm)
    def post(self, request):
        UserModel(**request.param).save()
        return HttpResponse(return_content("200001"))


class UserView(View):
    # 修改
    def put(self, request, user_id):
        pass

    # 获取
    def get(self, request, user_id):
        if request.user_id == user_id:
            user = UserModel.objects.get(userId=user_id)
            if user:
                return HttpResponse(return_content("200001", user.detail()))
            return HttpResponseNotFound(return_content("404001"))
        return HttpResponseForbidden(return_content("403001"))


# 获取用户主页
class IndexUserView(View):
    def get(self, request, user_id):
        user = UserModel.objects.get(userId=user_id)
        if user:
            return HttpResponse(return_content("200001", user.index()))
        return HttpResponseNotFound(return_content("404001"))
