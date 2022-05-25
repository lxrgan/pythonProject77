# -*- coding: utf-8 -*-
import requests as requests

import urllib3
def request_demo():
    url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    param={
        "corpid":"wwc46b9aac93930384",
        "corpsecret":"pYdG0PjmLsucSUZV8XNhA8KfpVOSXUie8eEV684fbt0"
    }
    proxy={
        "http":"http://127.0.0.1:8080",
        "https":"http://127.0.0.1:8080"
    }

    res=requests.get(url=url,params=param,proxies=proxy,verify=False)

if __name__=='__main__':
    request_demo()



