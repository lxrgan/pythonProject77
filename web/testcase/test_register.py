# -*- coding: utf-8 -*-
from time import sleep

from web.wechat_login_page.main_page import Main_Page


class TestRegister:
    def test_register(self):
        main=Main_Page()
        main.goto_register().register()
        sleep(10)
    def test_register1(self):
        main=Main_Page()
        a=main.goto_register()
        a.register()
        sleep(6)
    def test_login_register(self):
        main=Main_Page()
        a=main.goto_login()
        a.goto_register().register()
        sleep(6)