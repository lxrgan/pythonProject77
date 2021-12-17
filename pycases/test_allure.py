# -*- coding: utf-8 -*-
import allure


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_Login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("登录页面")
        with allure.step("步骤3:输入用户名和密码"):
            print("输入用户名和密码")
        print("这是登录：测试用例，登录成功")
@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索成功")
    def test_search_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入搜索页面"):
            print("搜索页面")
        with allure.step("步骤3:输入搜索内容"):
            print("输入搜索")
        print("这是搜索：测试用例，搜索成功")
