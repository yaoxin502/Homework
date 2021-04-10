# age = int(input('输入年龄'))
# if age >18:
#        print(f'您输入的年龄是{age}','已成年，可以上网')
# else :
#     print(f'您输入的年龄是{age}','未成年，不能上网')


# a = int(input('输入年龄'))
# if a < 18:
#     print(f'您输入的年龄是{a}','童工，违法')
# elif (a >= 18 and a <=60):
#     print(f'您输入的年龄是{a}','正常工作年龄，合法')
# else:
#     print(f'您输入的年龄是{a}','退休')
# print('结束')



money = int(input('是否有钱'))
if money == 1:
    print('可以上车')
    seat = int(input('是否有座'))
    if seat == 1:
        print('可以坐着')
    else:
        print('站着')
else:
    print('不能上车')