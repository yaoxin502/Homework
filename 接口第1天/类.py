# class Washer():
#     def wash(self):
#         print('我会洗衣服')
#
# haier1 = Washer()
# haier2 = Washer()
# haier1.wash()
# haier2.wash()
#
# haier1.width = 500
# haier1.height = 800
# print(f'海尔洗衣机的宽度是{haier1.width}')

#空类
# class A():
#     pass

# class Washer():
#     def __init__(self):
#         self.width = 500
#         self.height = 800
#     def print_info(self):
#         print(f'洗衣机的宽度是{self.width}，高度是{self.height}')
#
# haier1 = Washer()
# haier1.print_info()
# print(f'海尔洗衣机宽度是{haier1.width}')


# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def print_info(self):
#         print(f'洗衣机的宽度是{self.width}，高度是{self.height}')
#
# haier1 = Washer(100,300)
# haier1.print_info()
#
# haier2 = Washer(400,800)
# haier2.print_info()


# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return '这是海尔洗衣机的说明书'
#
# haier1 = Washer(10,20)
# print(haier1)

# class Washer():
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def __del__(self):
#         print(f'{self}对象已经被删除')
#
# haier1 = Washer(10,20)
# # del haier1
# print(haier1)

'''
小猫爱吃鱼，小猫要喝水
'''
# class Cat():
#     def eat(self,food):
#         self.food = food
#         print(f'小猫爱吃{food}')
#     def drink(self,water):
#         self.water = water
#         print(f'小猫要喝{water}')
# c = Cat()
# c.eat('鱼')
# c.drink('水')

# '''
# 性别为男的梁超老师教测试
# 类:教师
# 属性：性别,名字
# 方法：教
# '''
#
# class Teacher():
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#
#     def teach(self,speak):
#
#         print(f'性别为{self.gender}的{self.name}老师教{speak}')
#
# t = Teacher('梁超','男')
# t.teach('测试')


'''
搬家具
类：家具，房子
属性:
家具：家具面积，家具名称
房子：总面积，房子剩余面积，家具列表
方法：放
'''
class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

class Home():
    def __init__(self,area):
        self.area = area
        self.free_area = area
        self.furniture = []

    def __str__(self):
        return f'房子占地面积{self.area}，剩余面积{self.free_area}，家具有{self.furniture}'

    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，放不进去。')

bed = Furniture('床',6)
jia1 = Home(1200)
jia1.add_furniture(bed)
sofa = Furniture('沙发',10)
jia1.add_furniture(sofa)
cabinet = Furniture('柜子',1190)
jia1.add_furniture(cabinet)
print(jia1)