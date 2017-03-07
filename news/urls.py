# coding=utf-8


from django.conf.urls import url


from views import NewssView, NewsView


urlpatterns = [
    url(r'^news$', NewssView.as_view()),
    url(r'^news/(?P<news_id>(\d){1,32})$', NewsView.as_view()),
    ]