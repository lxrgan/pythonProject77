# -*- coding: utf-8 -*-
"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""

from mitmproxy import ctx,http


class Counter:

    def request(self, flow:http.HTTPFlow):
        url=flow.request.pretty_url
        method=flow.request.method
        with open("D:/GitHub/pythonProject77/test_mock/template.txt") as f:

            # 拿到文本字符串数据
            data = f.read()
            new_data = data.format(method=method, url=url)
            # print(new_data)
        # 将替换好的数据信息写入模板文件
        with open("template.py", "w", encoding="utf-8") as f:
            f.write(new_data)
    def response(self,flow:http.HTTPFlow):
        pass

addons = [
    Counter()
]