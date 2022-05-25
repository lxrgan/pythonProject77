# -*- coding: utf-8 -*-
import logging
import os
import signal
import subprocess

import pytest

from ui_framework.page.logger import log


@pytest.fixture(scope="module",autouse=True)
def record():
    #用例运行前启动录屏
    cmd = "scrcpy -r file.mp4"
    # p = subprocess.Popen(args=cmd,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    print(p)
    yield
    # 用例结束运行前启动录屏
    os.kill(p.pid,signal.CTRL_C_EVENT)
