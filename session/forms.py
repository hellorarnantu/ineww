# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '17-3-14'

from django import forms


class SessionForm(forms.Form):
    account = forms.CharField(required=True, max_length=60)
    password = forms.CharField(required=True, max_length=256, min_length=1)
