# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


class Register_page:
    def __init__(self,driver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.XPATH,"//*[@id='corp_name']").send_keys("zhuce")
        Register_page(self.driver)