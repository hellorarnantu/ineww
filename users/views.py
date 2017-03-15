# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from .models import UserModel


class UsersView(View):
    def post(self, request):
        pass


class UserView(View):
    def put(self, request, user_id):
        pass

    def get(self, request, user_id):
        pass


class IndexUserView(View):
    def get(self, request, user_id):
        pass
