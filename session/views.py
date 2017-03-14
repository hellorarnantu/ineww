# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '17-3-14'

from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from django.http import HttpResponse
from .forms import SessionForm
from utils.form_utils import dec_validate_form
from users.models import UserModel


class SessionView(View):
    @dec_validate_form(SessionForm)
    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass
