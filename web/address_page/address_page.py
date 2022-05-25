# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self,driver):
        self.driver=driver
    def add_member(self):
        def wait_name(driver):
            eles=driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')
            eles[-1].click()
            # if len(eles)< 3:
            #     eles[0].click()
            # else:
            #     eles[1].click()
            eles = driver.find_elements(By.XPATH, '//*[@id="username"]')
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        # sleep(10)
        # self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[1].click()
        # #输入姓名
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("测试19")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("ceshi19")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("13028980008")
        # 保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()


