# class Dog():
#     tooth = 10
# wangcai = Dog()
# xiaohei = Dog()
# Dog.tooth = 12
# wangcai.tooth = 20
# print(Dog.tooth)
# print(wangcai.tooth)
# print(xiaohei.tooth)

# class Dog():
#     def __init__(self):
#         self.age = 5
#     def info_print(self):
#         print(self.age)
# wangcai = Dog()
# # print(wangcai.age)
# # wangcai.info_print()
# print(Dog.age)

class Dog():
    __tooth = 10
    @classmethod
    def get_tooth(cls):
        return cls.__tooth
wangcai = Dog()
result = wangcai.get_tooth()
res = Dog.get_tooth()
print(result)
print(res)

# class Dog():
#     __tooth = 10
#     @staticmethod
#     def info_print():
#         print('狗类')
# wangcai = Dog()
# wangcai.info_print()
# Dog.info_print()