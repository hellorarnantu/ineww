# coding=utf-8

from django.conf.urls import url


from views import PhoneCodeView


urlpatterns = [
    url(r'^code/phone$', PhoneCodeView.as_view()),
    ]
