#求100以内的质数（只能被1和它本身整除）
'''
本题需要两个循环完成
内循环：该数除以比该数小的所有数，除了1和本身之外余数不能等于0，满足条件，否则跳出
外循环：100个数循环一遍
'''
list1 = []
i = 2
for i in range(2,101):
    j = 2
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list1.append(i)
print(list1)