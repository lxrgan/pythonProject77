# -*- coding: utf-8 -*-
import allure
from selenium.webdriver.common.by import By

from ui_framework.page.logger import log


def handle_black(fun):
    def run(*args,**kwargs):
        #需要过滤的弹窗
        black_list = ['//*[@resource-id="com.xueqiu.android:id/gt_one_login_nav_iv"]']
        #相当于self
        instance = args[0]
        try:
            log.debug("find"+args[2])
            return fun(*args,**kwargs)
        except Exception:
            # with open("./tmp.png","rb")as f:
            #     allure.attach(f.read(),attachment_type=allure.attachment_type.PNG)
            allure.attach(instance.screenshot(),attachment_type=allure.attachment_type.PNG)
            # instance.driver.save_screenshot("tmp.png")
            # 取出所有的屏蔽信息，进行处理
            for ele_xpath in black_list:
                # 检查屏蔽信息是否存在
                eles = instance.finds(By.XPATH, ele_xpath)
                # 如果屏蔽信息存在，进行点击处理
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args,**kwargs)


    return run