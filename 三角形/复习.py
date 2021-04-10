'''
print 123
'''

# a = 1
# print(type(a))
# b = 1.11
# print(type(b))
# c = False
# print(type(c))
# d = 'haha'
# print(type(d))
# e = [1,2,3]
# print(type(e))
# f = (1,2,3)
# print(type(f))
# g = {1,2,3}
# print(type(g))
# h = {'姓名':'张三','年龄':'18'}
# print(type(h))

# age = 18
# name = 'tom'
# weight = 75.5
# student_id = 1
# print('我的名字是%s' % name)
# print('我的学号是%03d' % student_id)
# print('我的体重是%.3f' % weight)
# print('我的名字是%s，今年%d岁了' % (name,age))
# print('我的名字是%s，明年%d岁了' % (name,age+1))
# print(f'我的名字是{name}，明年{age+1}岁了')

# pw = input('输入密码：')
# print(f'密码为{pw}')
# print(type(pw))
# print(type(int(pw)))

# list1 = [1,2,3]
# print(tuple(list1))
# print(type(tuple(list1)))

# str1 = '10'
# str2 = '[1,2,3]'
# str3 = '(22,33,44)'
# print(type(eval(str1)))
# print(type(eval(str2)))
# print(type(eval(str3)))

# num1 = 10
# float1 = 0.5
# str1 = 'hello'
# print(num1,float1,str1)

# a = 7
# b = 5
# print(a == b)

# money = int(input('是否有钱'))
# if money == 1:
#     print('可以上车')
#     seat = int(input('是否有座'))
#     if seat == 1:
#         print('可以坐下')
#     else:
#         print('无座，站着')
# else:
#     print('不能上车')


# import random
# com = random.randint(1,9)
# print(com)

# a = 1
# b = 2
# c = a if a > b else b
# print(c)

# i = 2
# su = 0
# while i <= 100:
#     su += i
#     i += 2
# print(su)

i = 1
su = 0
while i <= 100:
    if i % 2 == 1:
        su += i
    i += 1
print(su)