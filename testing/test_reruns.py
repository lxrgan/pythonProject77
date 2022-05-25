# -*- coding: utf-8 -*-
import pytest


@pytest.mark.flaky(reruns=4,reruns_delay=2)
def test_reruns():
    assert 1==2
    assert 2==2
    print("reruns")