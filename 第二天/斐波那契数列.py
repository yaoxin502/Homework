#求斐波那契数列 1 1 2 3 5 8 13 ……
# list1 = []
# a1 = 1
# a2 = 1
# for i in range(10):
#     num = a1 + a2
#     a2 = a1
#     a1 = num
#     list1.append(num)
# print(list1)

'''
n表示位数
第一位数和第二位数都是1
第三位数是第一第二位数的加和
递归：内部调用函数自己
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

for i in range(1,10):
    print(fib(i),end=' ')

# list1 = [1,1]
# n = int(input('please write your number:'))
# for i in range(n):
#     num = list1[-1] + list1[-2]
#     list1.append(num)
# print(list1)
