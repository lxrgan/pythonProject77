# -*- coding: utf-8 -*-
#启动app,停止app,重启app
import yaml
from appium import webdriver

from app.apppo.page.basepage import BasePage
from app.apppo.page.mainpage import MainPage

with open("../datas/caps.yaml")as f:
    datas=yaml.safe_load(f)
    desires=datas['desirecaps']
    ip=datas['server']['ip']
    port=datas['server']['port']

class App(BasePage):
    #启动app
    def start(self):
        if self.driver==None:
            #启动app
            # caps={}
            # caps["platformName"]="android"
            # caps["deviceName"]="EKCDU20915004223"
            # caps["appPackage"]="com.tencent.wework"
            # caps["appActivity"]=".launch.LaunchSplashActivity"
            # caps["noReset"]="true"

            #客户端与appium服务器建立连接的代码
            # self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
            self.driver=webdriver.Remote(f"http://{ip}:{port}/wd/hub",desires)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self
    def restart(self):
        #重启app
        self.driver.close_app()
        self.driver.launch_app()
    def stop(self):
        #停止app
        self.driver.quit()
    #进入app主页
    def goto_main(self):
        return MainPage(self.driver)

