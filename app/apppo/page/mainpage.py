# -*- coding: utf-8 -*-
#主页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from app.apppo.page.addresslistpage import AddressListPage
from app.apppo.page.basepage import BasePage

#进入主页页面
class MainPage(BasePage):
    addresslist_element=(MobileBy.XPATH,'//*[@text="通讯录"]')
    #点击通讯录
    def goto_addresslist(self):
        #点击通讯录
        #*self 解元组
        self.find(*self.addresslist_element).click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #进入通讯录页面
        return AddressListPage(self.driver)



