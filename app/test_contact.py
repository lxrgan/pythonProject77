# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


class TestContact:
    def setup(self):
        caps={}
        caps["platformName"]="android"
        caps["deviceName"]="EKCDU20915004223"
        caps["appPackage"]="com.tencent.wework"
        caps["appActivity"]=".launch.LaunchSplashActivity"
        caps["noReset"]="true"
        #跳过安装uiautomator2server等 服务
        caps["skipServerInstallation"]="true"
        #跳过设备的初始化
        caps["skipDeviceInitialization"]="true"
        #运行前不停止app
        # caps["dontStopAppOnReset"]="true"


        #客户端与appium服务器建立连接的代码
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    #滑动查找封装
    def swipe_find(self,text,num=3):
        for i in range(num):
            if i==num-1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次，未找到！")
            self.driver.implicitly_wait(1)
            try:
                element=self.driver.find_element(MobileBy.XPATH,f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size=self.driver.get_window_size()
                width=size.get('width')
                height=size.get('height')

                start_x=width/2
                start_y=height*0.8

                end_x=start_x
                end_y=height*0.3

                self.driver.swipe(start_x,start_y,end_x,end_y,1000)

            # return element


    def test_addcontact(self):
        name="jinlinshi_12"
        phonenum="13828790012"
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        element=self.swipe_find("添加成员")
        element.click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"姓名")]/../*[@text="必填"]').send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[contains(@text,"手机")]/..//*[@text="必填"]').send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成功"]')
    def test_delcontact(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/kl0').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="搜索"]').send_keys("jinlinshi_011")
        elelist=self.driver.find_elements(MobileBy.XPATH,'//*[@text="jinlinshi_011"]')
        if len(elelist)>1:
            elelist[1].click()




