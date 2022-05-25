# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from web.wechat_login_page.register_page import Register_page


class Login_Page:
    def __init__(self,driver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.XPATH,"//*[@class='login_registerBar_link']").click()
        return Register_page(self.driver)
