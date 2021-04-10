#1.冒泡排序
# li=[10,2,3,5,110,55,99,88,66]
# def bubble_sort(li):
#     for i in range(0,len(li)):
#         for j in range(i+1,len(li)):
#             if li[i]>li[j]:
#                 li[i],li[j]=li[j],li[i]
#     return li
# print(bubble_sort(li))

# 2.快速排序
# li = [3,6,8,4,56,89,34,88]
# def quick_sort(li):
#     if len(li) < 2:
#         return li
#     # 选取基准，随便选哪个都可以，选中间的便于理解
#     mid = li[len(li)//2]
#     # 定义基准值左右两个数列
#     right = []
#     left = []
#     # 从原始数组中移除基准值,大于基准值放右边,# 小于基准值放左边
#     li.remove(mid)
#     for i in li:
#         if i >= mid:
#             right.append(i)
#         else:
#             left.append(i)
#     return quick_sort(left) + [mid] + quick_sort(right)
# print(quick_sort(li))


#3.有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
# str = 'abcdef'
# li = list(str)
# n = 0
# while n < len(li)/2:
#     tmp = li[n]
#     li[n] = li[len(li)-n-1]
#     li[len(li) - n - 1] = tmp
#     n+=1
# print(''.join(li))

#4.li = [4,7,8,2,6,9]取最大值
# li = [4,7,8,2,6,9]
# maxnum = li[0]
# for i in li:
#     if i > maxnum:
#         maxnum = i
# print(i)

# 5.有一堆字符串，“aabbbcddef”，输出abcdef(去重)
# str = 'aabbbcddef'
# li = []
# for i in str:
#     if i not in li:
#         li.append(i)
# print(''.join(li))

# 6.列表中查找出现次数过半的数
# li = [1,3,3,3,3,5]
# list1 = []
# def more_than_half_num(li):
#     for i in li:
#         if li.count(i) > len(li)/2:
#             return i
# print(more_than_half_num(li))

# 7.有一组“+”和“-”符号，要求将“+”排到左边，“-”排到右边，写出具体的实现方法。
data = ['-','+','-','+','+']
def Data(data):
    for j in range(len(data)):
        for i in range(len(data)-1):
            if data[i] == '-':
                data[i],data[i+1] = data[i+1],data[i]
                i += 1
            else:
                i += 1
        j += 1
    return data
print(Data(data))


