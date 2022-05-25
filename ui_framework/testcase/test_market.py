# -*- coding: utf-8 -*-
from ui_framework.page.app import App
from ui_framework.page.logger import log_init


class TestMarket:
    def setup(self):
        self.app=App()
        log_init()
    def test_goto_market(self):
        self.app.start().goto_main().goto_market().goto_search().search()
        print("运行完成")