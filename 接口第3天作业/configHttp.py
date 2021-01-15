'''
功能描述：接受readExcel传入的接口请求测试数据，根据具体的请求逻辑完成接口测试，将接口返回的关键结果返回给用例即可
编写人：
编写日期：

步骤分析：
    1-接受readExcel传入的测试数据
    2-断言函数
        比对接口返回的实际错误码和预期错误码
                相等=success
                不等=fail
'''
import requests,xlrd
from common.readExcel import ReadExcel
class ConfigHttp():
    def __init__(self):
        self.d = ReadExcel()
        self.datalist2 = self.d.read()
        self.urlstr = self.datalist2[0][1]
        self.payload = eval(self.datalist2[0][4])
        self.method = self.datalist2[0][3]
        self.expect = self.datalist2[0][5]
        print(self.datalist2)

    def run(self,data):
        if str(data) == str(self.expect):
            print('success')
        else:
            print('fail')

if __name__ == '__main__':
    con = ConfigHttp()

