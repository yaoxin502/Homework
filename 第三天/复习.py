# def line():
#     print('-'*20)
#
# def lines():
#     for i in range(5):
#         line()
# lines()



# def sum_num(a, b, c):
#  return a + b + c
# result = sum_num(1, 2, 3)
# print(result)
# def average_num(a, b, c):
#  sumResult = sum_num(a, b, c)
#  return sumResult / 3
# result = average_num(1, 2, 3)
# print(result)

# a = 1
# b = a
# print(b)
# a = 2
# print(b)




# info = []
# def add_info():
#     new_name = input('请输入姓名：')
#     new_pwd = input('请输入密码：')
#     global info
#     for i in info:
#         if i['name'] == new_name:
#             print('该用户已存在。')
#             return
#     info_dict = {}
#     info_dict['name'] = new_name
#     info_dict['pwd'] = new_pwd
#     info.append(info_dict)
#     print(info)
# # add_info()
#
# while True:
#     add_info()




# list1 = [3,2,1,5,4,0,2]
# list2 = []
# for i in list1:
#     i = i ** 2
#     list2.append(i)
# print(list2)
#
# set1 = {i**2 for i in list1}
# print(set1)

# list1 = ['tom']
# list2 = ['20']
# dict1 = {}
# for i in list1:
#     for j in list2:
#         dict1['name'] = i
#         dict1['age'] = j
# print(dict1)

# n = int(input('请输入加到哪项：'))
# def sum_number(num):
#     if num == 1:
#         return 1
#     return num + sum_number(num-1)
# sum_result = sum_number(n)
# print(sum_reslut)

# i = int(input('输入第几位数：'))
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# fib_result = fib(i)
# print(fib_result)



# list1 = [1,2,3,4,5,5,2,3,2,4]
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# dict1 = {'lucy':21,'tom':30,'xiaoming':18,'xiaohong':15,'xiaowang':20,'xiaohei':19}
# dict2 = {key:value for key,value in dict1.items() if value > 18}
# print(dict2)

# list1 = [i for i in range(1,101) if i%3 == 0]
# print(list1)

# list1 = ['1','2','3']
# list1[0] = 1
# list1[1] = 2
# list1[2] = 3
# print(list1)


str1 = 'welocme to super&Test'
list1 = list(str1.split(' ')[0])
list2 = list(str1.split(' ')[1])
list3 = list(str1.split(' ')[2])
list1.reverse()
list2.reverse()
list3.reverse()
list4 = list1 + list2 + list3
print(''.join(list4))








