'''
3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
'''
'''
类1:房子
属性:户型，总面积，家具列表
类2：家具
属性：名字，占地面积
方法：摆放
'''
class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

class House():
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.furniture_list = []
    def __str__(self):
        return f'房子的户型是{self.house_type}，总面积是{self.area}，剩余面积是{self.free_area}，家具有{self.furniture_list}'

    def move(self,item):
        if self.free_area >= item.area:
            self.furniture_list.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，放不进去了。')

bed = Furniture('床',4)
closet = Furniture('衣柜',2)
table = Furniture('餐桌',1.5)
jia1 = House('两居室',100)
jia1.move(bed)
jia1.move(closet)
jia1.move(table)
print(jia1)





