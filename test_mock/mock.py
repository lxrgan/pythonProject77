# -*- coding: utf-8 -*-
"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import ctx,http


class Counter:
    # def __init__(self):
    #     self.num = 0

    def request(self, flow:http.HTTPFlow):
        # self.num = self.num + 1
        # ctx.log.info("We've seen %d flows" % self.num)
        flow.request
    def response(self,flow:http.HTTPFlow):
        #判断请求的url 是否包含指定的url
        if "https://stock.xueqiu.com/v5/stock/screener/quote/list.json?order="in flow.request.pretty_url:
            #拿到响应信息
            data=json.loads(flow.response.text)
            # data =flow.response.text
            # print(type(data))
            data["data"]["list"][1]["name"]="jinlinshi"
            flow.response.text=json.dumps(data)
            # flow.response.text=data
            # print(flow.response.txt)

addons = [
    Counter()
]