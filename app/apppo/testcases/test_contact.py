# -*- coding: utf-8 -*-
import yaml

from app.apppo.page.app import App


class TestContact():
    #测试进入主页面
    def setup(self):
        self.app=App().start()
        self.main=self.app.goto_main()
    def teardown(self):
        self.app.stop()
    #测试进入添加成员步骤
    def test_addcontact(self):
        name="jinlinshi_18"
        phonenum="13828790018"
        editpage=self.main.goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name,phonenum)
        editpage.veify_ok()

    def test_yaml(self):
        with open("../datas/caps.yaml") as f:
            datas = yaml.safe_load(f)
            # desires = datas['desirecaps']
            # ip = datas['server']['ip']
            # port = datas['server']['port']
            print(datas)

