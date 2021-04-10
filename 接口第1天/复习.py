'''
类:地瓜
属性：烤的时间，地瓜状态，调料列表
方法：烤，加调料
'''
# class Potato():
#     def __init__(self):
#         self.cook_time = 0
#         self.cook_static = '生的'
#         self.condiments_list = []
#     def cook(self,time):
#         self.cook_time += time
#         if 0 <= self.cook_time <3:
#             self.cook_static = '生的'
#         elif 3 <= self.cook_time < 5:
#             self.cook_static = '半生不熟'
#         elif 5 <= self.cook_time < 8:
#             self.cook_static = '熟了'
#         elif self.cook_time > 8:
#             self.cook_static = '烤糊了'
#     def add_condiments(self,condiment):
#         self.condiments_list.append(condiment)
#     def __str__(self):
#         return f'这个地瓜烤了{self.cook_time}分钟，地瓜状态是{self.cook_static}，加的调料有{self.condiments_list}。'
#
# digua1 = Potato()
# digua1.cook(2)
# digua1.add_condiments('甘梅')
# digua1.cook(4)
# digua1.add_condiments('盐')
# print(digua1)


# class Master():
#     def __init__(self):
#         self.kongfu = '五香'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
# class School(Master):
#     def __init__(self):
#         self.kongfu = '香辣'
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#         super().__init__()
#         super().make_cake()
#
# class Prentice(School):
#     def __init__(self):
#         self.kongfu = '独创'
#         #私有属性
#         self.__money = 2000
#     #私有方法
#     def __info_print(self):
#         print(self.kongfu)
#         print(self.__money)
#     def make_cake(self):
#         print(f'运用{self.kongfu}制作煎饼果子')
#
#     def make_old_cake(self):
#         super().__init__()
#         super().make_cake()
#     def make_master_cake(self):
#         Master.__init__(self)
#         Master.make_cake(self)
#     def make_school_cake(self):
#         School.__init__(self)
#         School.make_cake(self)
#
#     def get__money(self):
#         return self.__money
#
#     def set__money(self):
#         self.__money = 500
#     def __info_print(self):
#         print(self.kongfu)
#         print(self.__money)
#
#
#
# xiaoming = Prentice()
# # xiaoming.make_old_cake()
# # xiaoming.make_cake()
# # xiaoming.make_master_cake()
# # xiaoming.make_school_cake()
# xiaoming.set__money()
# print(xiaoming.get__money())

# class Dog():
#     __tooth = 10
#     @classmethod
#     def get_tooth(cls):
#         print('类方法')
# wangcai = Dog()
# wangcai.get_tooth()

# class Gun():
#     def __init__(self,model,bullet_count):
#         self.model = model
#         self.bullet_count = bullet_count
#     def shoot(self):
#         if self.bullet_count == 0:
#             print('请先装填子弹。')
#         else:
#             self.bullet_count -= 1
#             print(f'射击成功,还剩{self.bullet_count}颗子弹。')
#     def add_bullet(self,count):
#         self.bullet_count += count
#         print(f'已经装填了{count}颗子弹。')
#     def __str__(self):
#         return f'{self.model}有{self.bullet_count}颗子弹'
#
# class Soldier():
#     def __init__(self,name):
#         self.name = name
#
#     def fire(self,item):
#         item.shoot()
#         item.add_bullet(20)
#     def __str__(self):
#         return f'士兵{self.name}'
#
# g1 = Gun('AK47',10)
# s1 = Soldier('Ryan')
# s1.fire(g1)
# print(s1)
# print(g1)




