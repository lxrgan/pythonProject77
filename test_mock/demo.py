# -*- coding: utf-8 -*-
def demo():
    with open("template.txt") as f:
        #拿到文本字符串数据
        data  = f.read()
        new_data=data.format(method="get",url="www.baidu.com")
        # print(new_data)
    #将替换好的数据信息写入模板文件
    with open("template.py","w",encoding="utf-8")as f:
        f.write(new_data)
if __name__=='__main__':
    demo()

