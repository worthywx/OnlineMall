from django.views.generic.base import View

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        商品列表页视图
        :param request:
        :return:
        """
        res_list = []
        goods = Goods.objects.all()[:10]

        from  django.http import HttpResponse
        from django.core import serializers
        json_data = serializers.serialize("json", goods)
        import json
        return HttpResponse(json_data, content_type="application/json")