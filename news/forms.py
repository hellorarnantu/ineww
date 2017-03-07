# coding=utf-8


import json

from django import forms


class NewsPageForm(forms.Form):
    page = forms.IntegerField(required=False, min_value=1)
    page_per = forms.IntegerField(required=False, min_value=5, max_value=100)

    def clean(self):
        cleaned_data = super(NewsPageForm, self).clean()
        page = cleaned_data.get('page', 1)
        page_per = cleaned_data.get('page_per', 10)
        cleaned_data['page'] = page if page else 1
        cleaned_data['page_per'] = page_per if page_per else 10
