# -*- coding: utf-8 -*-
import pytest


class TestDemo:
    def test_a(self):
        print("a")

    def test_b(self):
        print("b")

def fun(a):
    a=a-1
def test_a():
    print("211211TY4RGUTP pytest")
def test_answer():
    assert fun(3)==5
if __name__ == '__main__':
    # pytest.main("test_a.py")
    pytest.main(['test_a.py::TestDemo','-v'])