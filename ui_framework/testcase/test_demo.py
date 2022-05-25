# File  : test.py
# IDE   : PyCharm

import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)   # 输出等级
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   # 输出格式

handler = logging.FileHandler("log.txt")    # 文本输出
handler.setFormatter(formatter)
console = logging.StreamHandler(sys.stdout)   # 控制台输出
console.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(console)

if __name__ == '__main__':
    logger.info("这是一条info级别信息")
    logger.debug("这是一条debug级别信息")
    logger.warning("这是一条warning级别信息")