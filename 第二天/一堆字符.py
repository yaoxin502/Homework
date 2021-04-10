# 有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
# str1 = 'aabbbcddef'
# for i in str1:
#     if str1.count(i) == 1:
#         print(i,end='')
#
# 有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
# str1 = 'welocme to super&Test'
# for i in ((str1.split(' ')[-1]).split('&')):
#     print(i,end='')
#
# 有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
# str1 = 'welocme to super&Test'
# print(str1[::-1])
#
# 有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
# str1 = 'abcdef'
# i = len(str1) - 1
# list1 = []
# while(i >= 0):
#     list1.append(str1[i])
#     i = i - 1
# for i in list1:
#     print(i,end='')

#方法2
str1 = 'abcdef'
str2 = list(str1)
n = 0
while n < len(str2)/2:
    tmp = str2[n]
    str2[n] = str2[len(str2)-n-1]
    str2[len(str2)-n-1] = tmp
    n += 1
print(''.join(str2))

#
# 有一堆字符串，“aabbbcddef”，输出abcdef
# str1 = 'aabbbcddef'
# list1 = []
# for i in str1:
#     if i not in list1:
#         list1.append(i)
#         print(i,end='')
#
#
#
#
str1 = 'welocme to super&Tes'
str1.split(' ')
list1 = list(str1)
list1.reverse()
for i in list1:
    print(i,end='')