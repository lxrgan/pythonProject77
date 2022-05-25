# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy

from app.apppo.page.basepage import BasePage

##进入编辑添加联系人页面
class EditContactPage(BasePage):
    #编辑页面添加联系人姓名、手机号
    def edit_contact(self,name,phonenum):
        self.find(MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.find(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phonenum)
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
    #添加完成验证是否添加成功
    def veify_ok(self):
        self.find(MobileBy.XPATH,'//*[@text="添加成功"]')
