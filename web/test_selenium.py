# -*- coding: utf-8 -*-
import json
from time import sleep

from selenium import webdriver


class TestTmp():

    def setup_method(self,method):
        """
        浏览器复用
        chrome -remote-debugging-port=9222
        :param method:
        :return:
        """
        #声明Chrome参数
        chrome_arg=webdriver.ChromeOptions()
        #加入调试地址
        chrome_arg.debugger_address='127.0.0.1:9222'
        #复用方式
        self.driver = webdriver.Chrome(options=chrome_arg)
        #非复用方式
        # self.driver = webdriver.Chrome()
        self.vars={}

    def teardown_method(self,method):
        self.driver.quit()
    def test_tmp(self):
        # self.driver.get("https://work.weixin.qq.com/")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.close()

    def test_cookie_login(self):
        """
        利用cookie进行登录
        :return:
        """
        """
        存入cookie
        """
        # cookies=self.driver.get_cookies()
        # with open("tmp.txt","w",encoding="utf-8")as f:
        #     json.dump(cookies,f)
        # 读取cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp.txt","r",encoding="utf-8")as f:
            cookies=json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)