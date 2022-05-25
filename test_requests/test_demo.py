# -*- coding: utf-8 -*-
import json

import requests


class TestAddress:
    def setup(self):
        self.token=self.get_token()
    def get_token(self):
        """
        corpid:"wwc46b9aac93930384"
        corpsecret:"NS9K_pMlHbQ2u8ZllARINazYvxY2mxYqM3sx2LemyTY"
        :return:
        """
        # requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET")
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwc46b9aac93930384&corpsecret=NS9K_pMlHbQ2u8ZllARINazYvxY2mxYqM3sx2LemyTY")
        # print(r.text)
        return r.json()['access_token']

    def test_get_infomation(self):
        user_id="jinlinshizd_01"
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}")
        print(r.json())

    def test_create_member(self):
        proxies={"https":"http://127.0.0.1:8099"}
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data={"userid": "jinlinshizd_03",
	            "name": "锦霖誓自动03",
	            "mobile": "+86 13800000013",
	            "department": [1]}
        # r=requests.post(url,json.dumps(data))
        r=requests.post(url,json=data,proxies=proxies,verify=False)
        print(r.json())
    def test_update_member(self):
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data={"userid": "jinlinshizd_01",
              "name":"锦霖誓自动二"}
        r=requests.post(url,json=data)

    def test_delete_member(self):
        user_id="jinlinshizd_02"
        url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"

        r=requests.get(url)
        print(r.json())


