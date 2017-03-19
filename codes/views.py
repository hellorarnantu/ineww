# coding=utf-8


from __future__ import absolute_import
from __future__ import unicode_literals

from .forms import PhoneCodeForm
from django.views import View
from utils.form_utils import dec_validate_form
from django.http import HttpResponse
from utils.code_utils import send_code
from utils.common_utils import return_content


class PhoneCodeView(View):
    @dec_validate_form(PhoneCodeForm)
    def post(self, request):
        send_code(phone=request.param["phone"])
        return HttpResponse(status=204, content=return_content("204001"))
