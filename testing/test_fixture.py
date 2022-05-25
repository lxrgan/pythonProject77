# -*- coding: utf-8 -*-
import datetime

import pytest



# @pytest.fixture()
# def get_username():
#     name="赵武"
#     print(f"用户名是：{name}")
#     return "name"

def test_search():
    print("搜索")

def test_cart(login):
    print("购物")
    print(login)

def test_order(login):
    print("下单")