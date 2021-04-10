# class Master():
#     def __init__(self):
#         self.konfu = '配方'
#
#     def make(self):
#         print(f'运用{self.konfu}做蛋糕')
#
# class School():
#     def __init__(self):
#         self.konfu = '香辣配方'
#     def make(self):
#         print(f'运用{self.konfu}做煎饼果子')
#
# class Prentice(School,Master):
#     def __init__(self):
#         self.konfu = '独创秘方'
#     def make(self):
#         print(f'运用{self.konfu}做')
# xiaoming = Prentice()
# print(xiaoming.konfu)
# xiaoming.make()
#
# print(Prentice.__mro__)


class Master():
    def __init__(self):
        self.konfu = '五香配方'
        self.__money = 200
    def make(self):
        print(f'运用{self.konfu}做煎饼果子')

class School(Master):
    def __init__(self):
        self.konfu = '香辣配方'
    def make(self):
        print(f'运用{self.konfu}做煎饼果子')
        super().__init__()
        super().make()

class Prentice(School):
    def __init__(self):
        self.konfu = '独创秘方'
    def make(self):
        self.__init__()
        print(f'运用{self.konfu}做')




    # def make_master(self):
    #     Master.__init__(self)
    #     Master.make(self)
    #
    # def make_school(self):
    #     School.__init__(self)
    #     School.make(self)

    def make_old(self):
        super().__init__()
        super().make()

xiaoming = Prentice()
#xiaoming.make_old()
# print(xiaoming.__money)
#xiaoming.make_school()
xiaoming.make_old()
#xiaoming.make()