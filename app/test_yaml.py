# -*- coding: utf-8 -*-
import logging

import yaml
#日志输出
# root_log=logging.getLogger()
logging.getLogger().setLevel(logging.DEBUG)
#json转换为yaml格式
def test_yam():
    logging.info("test_yaml")
    yamll={'desirecaps': {'platformName': 'android', 'deviceName': 'EKCDU20915004223', 'appPackage': 'com.tencent.wework', 'appActivity': '.launch.LaunchSplashActivity', 'noReset': 'true'}, 'server': {'ip': '127.0.0.1', 'port': 4723}}
    print(yaml.safe_dump(yamll))
    logging.info(yaml.safe_dump(yamll))


