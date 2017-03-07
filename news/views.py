# coding=utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.views import View
from .models import NewsModel
from utils.form_utils import dec_validate_form
from .forms import NewsPageForm
from django.http import HttpResponse
from utils.common_utils import return_content

class NewsView(View):
    def get(self, request, news_id):
        news = NewsModel.objects.filter(
            news_id=news_id
        ).first()
        data = {}
        if news:
            data = news.detail()
        return HttpResponse(return_content("200001", data))


class NewssView(View):


    @dec_validate_form(NewsPageForm)
    def get(self, request):
        page = request.data['page']
        page_per = request.data['page_per']
        query_list = NewsModel.objects.all()
        count = query_list.count()
        news_list= query_list.only(
            "news_id", "title", "image", "author", "created_time", "keywords", "source", "brief", "category"
        ).order_by("-created_time")[(page-1)*page_per:page*page_per]
        result = [
            news.info() for news in news_list
        ]
        return HttpResponse(return_content("200001", {
            "page":page,
            "page_per":page_per,
            "count":count,
            "result": result
        }))

