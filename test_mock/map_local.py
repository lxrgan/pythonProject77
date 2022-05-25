# -*- coding: utf-8 -*-

"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
import json

from mitmproxy import ctx,http
from mitmproxy import http


class Counter:
    # def __init__(self):
    #     self.num = 0

    def request(self, flow:http.HTTPFlow):
        # self.num = self.num + 1
        # ctx.log.info("We've seen %d flows" % self.num)
        """
        使用request时间实现map local
        :param flow:
        :return:
        """
        if "https://stock.xueqiu.com/v5/stock/screener/quote/list.json?order=" in flow.request.pretty_url:
            #给flow.response属性赋值
            #赋值 调用mitmproxy 响应对象的make方法
            #响应体make函数里面所需要的数据为str
            with open("D:/GitHub/pythonProject77/test_mock/xueqiu.json",encoding="utf-8")as f:
                flow.response=http.HTTPResponse.make(200,
                    f.read(),
                    {"Content-Type":"text/html"}
                     )
    def response(self,flow:http.HTTPFlow):
        """


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
              :param flow:
        :return:
        """
        pass

addons = [
    Counter()
]