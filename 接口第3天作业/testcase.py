'''
功能描述：
编写人：
编写日期：

步骤分析：
    1-导入common.configHttp模块，获取测试数据
    2-根据获取的接口的请求方式进行判断
        get-调用request.get()
        post-调用request.post()
    3-调用configHttp模块里的断言函数进行断言
    4.写入Excel
'''
import requests,xlrd
from common.configHttp import ConfigHttp
class TestCase():
    def __init__(self):
        self.c = ConfigHttp()

    def res1(self):
        if self.c.method.lower() == 'post':
            r = requests.post(url=self.c.urlstr,data=self.c.payload)
            real = r.json()['errorCode']
            print(real)
            #断言
            self.c.run(real)

    def res2(self):
        if self.c.method.lower() == 'get':
            r = requests.get(url=self.c.urlstr,params=self.c.payload)
            real = r.json()['errorCode']
            print(real)
            #断言
            self.c.run(real)

if __name__ == '__main__':
    t = TestCase()
    t.res1()
    t.res2()