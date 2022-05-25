# -*- coding: utf-8 -*-
import requests as requests


class Base:
    def __init__(self):
        #添加session提高速度
        self.s=requests.Session()
        self.token = self.get_token()
        #链接后面不用每次加token，只需要加入session
        self.s.params={"access_token":self.token}
    def get_token(self):
        """
        corpid:"wwc46b9aac93930384"
        corpsecret:"NS9K_pMlHbQ2u8ZllARINazYvxY2mxYqM3sx2LemyTY"
        :return:
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params={"corpid":"wwc46b9aac93930384","corpsecret":"NS9K_pMlHbQ2u8ZllARINazYvxY2mxYqM3sx2LemyTY"}
        # r = requests.get(url,params=params
        r = self.s.get(url,params=params
            )
        # print(r.text)
        return r.json()['access_token']
    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)