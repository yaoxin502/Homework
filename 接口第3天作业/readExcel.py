'''
步骤分析：
1.导入xlrd包
2.打开Excel（Excel路径+名称）
3.确定sheet页
4.确定所有数据的最大行数作为循环次数，定义保存数据的空列表
    4.1迭代读取Excel中每一行的数据
    4.2第一行数据（list1）作为字典的key，其余行数据（list2）遍历出来作为字典的value；用zip()函数把两个列表合成字典
    4.3把处理成字典格式的数据，追加进列表
5.return 测试数据
'''
import xlrd,os
class ReadExcel():
    def __init__(self):
        self.currenDir = os.path.dirname(os.path.dirname(__file__))
        self.excel = self.currenDir + '/testData/data.xls'
        self.readbook = xlrd.open_workbook(self.excel)
        self.sheet = self.readbook.sheet_by_name('testdata')
        self.nrows = self.sheet.nrows
    def read(self):
        datalist1 = []
        for i in range(0,self.nrows):
            row_value = self.sheet.row_values(i)
            datalist1.append(row_value)
        list1 = datalist1[0]
        list2 = datalist1[1:]
        datalist2 = []
        for j in list2:
            dict_row_value = dict(zip(list1,j))
            datalist2.append(dict_row_value)
        print(datalist2)
        return datalist1,datalist2

if __name__ == '__main__':
    r = ReadExcel()
    r.read()