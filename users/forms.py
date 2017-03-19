# coding=utf-8



from __future__ import absolute_import
from __future__ import unicode_literals
from .models import DoUserModel
from utils.common_utils import valid_phone

from django import forms


class UserSaveForm(forms.Form):
    username = forms.CharField(required=True, max_length=12, min_length=1)
    phone = forms.CharField(required=True, max_length=20, min_length=11)
    code = forms.CharField(required=True, max_length=4, min_length=4)
    pwd = forms.CharField(required=True, max_length=32, min_length=6)
    agree = forms.ChoiceField((('1', '1'),), required=True)

    def clean(self):
        cleaned_data = super(UserSaveForm, self).clean()
        if self.is_valid():
            if not valid_phone(cleaned_data["phone"]):
                self.errors["phone"] = "valid"


class UserUpdateForm(forms.Form):
    username = forms.CharField(required=False, max_length=12, min_length=1)
    address = forms.CharField(required=False, max_length=128, min_length=1)
    company = forms.CharField(required=False, max_length=128, min_length=1)
    gender = forms.ChoiceField(required=False, choices=(("0", "0"), ("1", "1"), ("2", "2")))
    signature = forms.CharField(required=False, max_length=63, min_length=1)
    avatar = forms.CharField(required=False, min_length=1, max_length=128)
    birthday = forms.DateField(required=False)
    tags = forms.CharField(required=False, min_length=1, max_length=20)

    def clean(self):
        cleaned_data = super(UserUpdateForm, self).clean()
        if self.is_valid():
            for k, _ in cleaned_data.items():
                if not _:
                    del cleaned_data[k]


class PwdForm(forms.Form):
    re_pwd = forms.CharField(required=True, max_length=32, min_length=6)
    pwd = forms.CharField(required=True, max_length=32, min_length=6)


class AccountForm(forms.Form):
    phone = forms.CharField(required=True, max_length=20, min_length=11)
    code = forms.CharField(required=True, max_length=4, min_length=4)

    def clean(self):
        cleaned_data = super(AccountForm, self).clean()
        if self.is_valid():
            if not valid_phone(cleaned_data["phone"]):
                self.errors["phone"] = "valid"


class PhoneForm(forms.Form):
    phone = forms.CharField(required=True, max_length=20, min_length=11)

    def clean(self):
        cleaned_data = super(PhoneForm, self).clean()
        if self.is_valid():
            if not valid_phone(cleaned_data["phone"]):
                self.errors["phone"] = "valid"
