from __future__ import absolute_import
from __future__ import unicode_literals

from django import forms
from utils.common_utils import valid_phone


class PhoneCodeForm(forms.Form):
    phone = forms.CharField(required=True, min_length=11, max_length=20)

    def clean(self):
        cleaned_data = super(PhoneCodeForm, self).clean()
        if self.is_valid():
            if not valid_phone(cleaned_data["phone"]):
                self.errors["phone"] = "valid"
