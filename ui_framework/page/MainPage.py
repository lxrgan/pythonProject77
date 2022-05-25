# -*- coding: utf-8 -*-
from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from ui_framework.page.basepage import BasePage
from ui_framework.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        #最原始
        # self.find_and_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_and_click(By.XPATH,'//*[@resource-id="android:id/tabs"]/android.widget.RelativeLayout[2]/android.widget.ImageView[1]')
        """


        # #关键字引用
        with open("../page/main_page.yaml","r",encoding="utf-8")as f:
            function = yaml.load((f.read()), Loader=yaml.FullLoader)
        #从关键字中取出一个函数
        steps = function.get("goto_market")
        for step in steps:
            #如果发现关键字是find_and_click，就调用已经封装好的find_and_click即可
            if step.get("action")=="find_and_click":
                self.find_and_click(step.get('locator'),step.get('value'))


        """
        #封装后使用函数
        self.parse("../page/main_page.yaml","goto_market")
        return Market(self.driver)
        # self.find_and_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]')
        # self.find_and_send(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/search_input_text"]',"阿里巴巴")