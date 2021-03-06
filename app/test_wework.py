# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestWeWork():
    def setup(self):
        caps={}
        caps["platformName"]="android"
        caps["deviceName"]="EKCDU20915004223"
        caps["appPackage"]="com.tencent.wework"
        caps["appActivity"]=".launch.LaunchSplashActivity"
        caps["noReset"]="true"

        #客户端与appium服务器建立连接的代码
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_daka(self):

        self.driver.find_element(MobileBy.XPATH,"// android.view.ViewGroup//*[@text='工作台']").click()
        # sleep(10)
        #移动页面
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true)'
                                 '.instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text = "外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"次外出")]').click()
        # assert "外出打卡成功"in self.driver.page_source
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡成功']")

