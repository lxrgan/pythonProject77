# -*- coding: utf-8 -*-
import requests as requests

from test_requests.wework.base import Base


class WeworkAddress(Base):


    def get_infomation(self,user_id:str):
        url="https://qyapi.weixin.qq.com/cgi-bin/user/get"
        # params={"access_token":self.token,"userid":user_id}
        params={"userid":user_id}
        # r = requests.get(url,params=params)
        # r = self.s.get(url,params=params)
        r = self.send("GET",url,params=params)
        # print(r.json())
        return r.json()

    def create_member(self,user_id:str,name:str,mobile:str,department:list):
        """

        :param name:
        :param mobile:11位梳子
        :param department:
        :return:
        """
        # proxies = {"https": "http://127.0.0.1:8099"}
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {"userid": user_id,
                "name": name,
                "mobile": mobile,
                "department":department}
        # r=requests.post(url,json.dumps(data))
        # r = requests.post(url, json=data)
        # r = self.s.post(url, json=data)
        r = self.send("POST",url, json=data)
        # print(r.json())
        return r.json()

    def update_member(self,user_id:str,name:str):
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {"userid": user_id,
                "name": name}
        # r = requests.post(url, json=data)
        # r = self.s.post(url, json=data)
        r = self.send("POST",url, json=data)
        return r.json()

    def delete_member(self,user_id):

        # user_id = "jinlinshizd_03"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        # params={"access_token":self.token,"userid":user_id}
        params={"userid":user_id}
        # r = requests.get(url,params=params)
        # r = self.s.get(url,params=params)
        r = self.send("GET",url,params=params)
        # print(r.json())
        return r.json()