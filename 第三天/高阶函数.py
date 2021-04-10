# def sum_num(a,b,f):
#     return f(a)+f(b)
# # result = sum_num(-1,2,abs)
# result = sum_num(1.2,1.9,round)
# print(result)

# list1=[1,2,3,4,5]
# def func(x):
#     return x ** 2
# result = map(func,list1)
# print(result)
# print(list(result))

import functools
list1 = [1,2,3,4,5]
def func(a,b):
    return a+b
result = functools.reduce(func,list1)
print(result)