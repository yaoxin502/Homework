# n = 0
# while n < 5:
#     print('你好,第%d遍' % (n+1))
#     n = n + 1

# n = 1
# sum = 0
# while n <= 100:
#     sum = sum + n
#     n = n + 1
# print('sum',sum)


#偶数相加
# n =0
# sum = 0
# while n <= 100:
#     sum = sum + n
#     n = n + 2
# print('sum',sum)

sum = 0
n = 1
while n <=100:
    if n%2 == 0:
        sum = sum + n
    n = n + 1
print(sum)

