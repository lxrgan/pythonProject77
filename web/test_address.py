# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Testaddress:
    def test_address(self):
        # 声明Chrome参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        # 复用方式
        self.driver = webdriver.Chrome(options=chrome_arg)
        # 非复用方式
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait("5")
        #点击通讯录
        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']").click()
        #查找元素 $x('//*[@class="qui_btn ww_btn js_add_member"]')[1]
        def wait_name(driver):
            self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[1].click()
            eles=driver.find_elements(By.XPATH, '//*[@id="username"]')
            return len(eles)>0
        WebDriverWait(self.driver,10).until(wait_name)
        # sleep(10)
        # self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[1].click()
        # #输入姓名
        self.driver.find_element(By.XPATH,'//*[@id="username"]').send_keys("测试16")
        #输入账号
        self.driver.find_element(By.XPATH,"//*[@id='memberAdd_acctid']").send_keys("ceshi16")
        #输入手机号
        self.driver.find_element(By.XPATH,"//*[@id='memberAdd_phone']").send_keys("13028980005")
        #保持
        self.driver.find_element(By.XPATH,"//*[@class='qui_btn ww_btn js_btn_save']").click()


