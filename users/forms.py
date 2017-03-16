# coding=utf-8



from __future__ import absolute_import
from __future__ import unicode_literals

from django import forms

class UserSaveForm(forms.Form):
    username = forms.CharField(required=True, max_length=12, min_length=1)
    phone = forms.CharField(required=True, max_length=20, min_length=11)
    code = forms.CharField(required=False, max_length=6)
    pwd = forms.CharField(required=True, max_length=32, min_length=6)
    agree = forms.ChoiceField((('1', '1'),), required=True)

class UserUpdateForm(forms.Form):
    username = forms.CharField(required=True, max_length=12, min_length=1)
    phone = forms.CharField(required=True, max_length=20, min_length=11)
    code = forms.CharField(required=False, max_length=6)
    pwd = forms.CharField(required=True, max_length=32, min_length=6)
