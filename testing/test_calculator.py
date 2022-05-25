# -*- coding: utf-8 -*-

import sys

import pytest
import yaml

sys.path.append('..')
from pythoncode.Calculator import Calculator

def get_datas():
    with open("./datas/calc.yaml") as f:
        datas=yaml.safe_load(f)
        print(datas)

class TestCalculator:
    #前置条件
    def setup(self):
        print("开始计算")
        self.calc=Calculator()
    def teardown(self):
        print("结束计算")
    # @pytest.mark.add
    @pytest.mark.parametrize("a,b,result",[[1,1,2],[100,200,300],[1,0,1]])
    def test_add(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a,b)
    # @pytest.mark.parametrize("a,b,result",[[1,1,2],1,2,3])
    # def test_add_float(self,a,b,result):
    #     print(f"a={a},b={b},result={result}")
    #     assert result == self.calc.add(a,b)
    # @pytest.mark.div
    #todo:相除功能
    def test_div(self):
        pass