# -*- coding: utf-8 -*-
#添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from app.apppo.page.EditContactPage import EditContactPage
from app.apppo.page.basepage import BasePage

#进入添加成员页面
class AddContactPage(BasePage):
    #点击手动输入添加
    def addcontact_menual(self):
        #手动输入添加
        self.find(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        #进入编辑添加联系人页面
        return EditContactPage(self.driver)