# coding=utf-8


from django.conf.urls import url


from views import SessionView


urlpatterns = [
    url(r'^session$', SessionView.as_view()),
    ]