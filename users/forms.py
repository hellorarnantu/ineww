# coding=utf-8



from __future__ import absolute_import
from __future__ import unicode_literals

from django import forms
class UserSaveForm(forms.Form):
    username = forms.CharField(required=True, max_length=12, min_length=1)
    account = forms.CharField(required=True, max_length=50, min_length=4)
    type = forms.ChoiceField(required=True, choices=type_choice)
    code = forms.CharField(required=False, max_length=6)
    pwd = forms.CharField(required=True, max_length=32, min_length=6)
    rePwd = forms.CharField(required=True, max_length=32, min_length=6)
    agree = forms.ChoiceField((('1', '1'),), required=True)

