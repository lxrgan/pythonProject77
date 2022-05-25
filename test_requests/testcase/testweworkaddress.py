# -*- coding: utf-8 -*-
import pytest

from test_requests.wework.weworkaddress import WeworkAddress


class TestWork:
    name = "jiekouzd_"
    user_id = "jlszd"
    def setup_class(self):
        self.address = WeworkAddress()
        self.mobile="13920000002"
        self.department=[1]
    def setup(self):
        self.user_id+="tmp"
        self.address.delete_member(self.user_id)
    def teardown(self):
        self.address.delete_member(self.user_id)


    def test_get_infomation(self):
        #数据处理
        self.address.create_member(self.user_id,self.name,self.mobile,self.department)
        #用户信息是否正确
        r=self.address.get_infomation(self.user_id)
        assert r["name"]==self.name

    def test_create_member(self):
        #数据处理
        # self.address.create_member()
        r=self.address.create_member(self.user_id,self.name,self.mobile,self.department)
        assert r.get("errmsg")=="created"

        #断言
        info=self.address.get_infomation(self.user_id)
        assert info['name']==self.name
    @pytest.mark.parametrize("user_id,new_name",[("tmp",name+"tmp")]*10)
    def test_update_member(self,user_id,new_name):
        user_id+=self.user_id
        self.address.create_member(user_id,self.name,self.mobile,self.department)
        # new_name=self.name+"up"
        r=self.address.update_member(user_id,new_name)
        assert r.get("errmsg")=="updated"
        #断言
        info=self.address.get_infomation(user_id)
        assert info['name']==new_name
    def test_delete_member(self):
        self.address.create_member(self.user_id,self.name,self.mobile,self.department)
        r=self.address.delete_member(self.user_id)
        assert r.get("errmsg")=="deleted"
        #断言
        info=self.address.get_infomation(self.user_id)
        assert info['errcode']==60111

