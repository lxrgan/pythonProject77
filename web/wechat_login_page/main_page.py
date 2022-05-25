# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from web.wechat_login_page.login_page import Login_Page
from web.wechat_login_page.register_page import Register_page


class Main_Page:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        self.driver.find_element(By.XPATH,"//*[@class='index_top_operation_loginBtn']").click()
        return Login_Page(self.driver)
    def goto_register(self):
        self.driver.find_element(By.XPATH,"//*[@class='index_head_info_pCDownloadBtn']").click()
        return Register_page(self.driver)


