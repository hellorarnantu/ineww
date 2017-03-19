# coding=utf-8

from django.conf.urls import url


from views import UserView, UsersView, IndexUserView, PwdView, AccountView


urlpatterns = [
    url(r'^user$', UsersView.as_view()),
    url(r'^user/(?P<user_id>(\w){32})$', UserView.as_view()),
    url(r'^user/pwd$', PwdView.as_view()),
    url(r'^user/phone$', AccountView.as_view()),
    url(r'^user/(?P<user_id>(\w){32})/index$', IndexUserView.as_view()),
    ]
