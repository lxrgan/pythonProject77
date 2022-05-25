# -*- coding: utf-8 -*-
import datetime

import pytest


@pytest.fixture(scope="session")
def login():
    print("登录操作")
    token=datetime.datetime.now()
    yield token   #yiled相当于return
    print("登出操作")
    return token