# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.address_page.address_page import AddressPage


class MainPage:
    def __init__(self):
        #复用登录  chrome -remote-debugging-port=9222
        chrome_arg=webdriver.ChromeOptions()
        #加入调试地址
        chrome_arg.debugger_address='127.0.0.1:9222'
        # 复用方式
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait("5")
        # self.driver.get("https://work.weixin.qq.com/")
    def goto_address(self):
        #点击通讯录
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)




