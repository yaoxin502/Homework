'''
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
'''
'''
分析：
类：人
属性：姓名，体重
方法：跑步，吃东西
'''
class People():
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步后体重是{self.weight}')

    def eat(self):
        self.weight += 1
        print(f'{self.name}吃东西后体重是{self.weight}')

p1 = People('小明',75.0)
p1.run()
p1.eat()
p2 = People('小美',45.0)
p2.run()
p2.eat()
