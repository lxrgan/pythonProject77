# -*- coding: utf-8 -*-
import yaml
from selenium.webdriver.common.by import By

from ui_framework.page.Search import Search
from ui_framework.page.basepage import BasePage


class Market(BasePage):
    def goto_search(self):
        #最原始
        # self.find_and_click(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]')
        # #关键字引用
        """
        with open("../page/market.yaml","r",encoding="utf-8")as f:
            function = yaml.load((f.read()), Loader=yaml.FullLoader)
        #从关键字中取出一个函数
        steps = function.get("goto_search")
        for step in steps:
            #如果发现关键字是find_and_click，就调用已经封装好的find_and_click即可
            if step.get("action")=="find_and_click":
                self.find_and_click(step.get('locator'),step.get('value'))
        """
        #使用封装后的函数
        self.parse("../page/market.yaml","goto_search")
        return Search(self.driver)


