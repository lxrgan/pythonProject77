# -*- coding: utf-8 -*-
import pytest
import yaml


class TestData:
    # @pytest.mark.parametrize("a,b",[(10,20),(20,30)])
    @pytest.mark.parametrize("a,b",yaml.safe_load(open('./a.yaml')))
    def test_a(self,a,b):

        print("a+b")