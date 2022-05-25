# -*- coding: utf-8 -*-
#通讯录页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from app.apppo.page.AddContactPage import AddContactPage
from app.apppo.page.basepage import BasePage

#进入通讯录页面
class AddressListPage(BasePage):

    #点击添加成员
    def click_addcontact(self):
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        element=self.swipe_find("添加成员")
        element.click()
        #进入添加联成员页面
        return AddContactPage(self.driver)

