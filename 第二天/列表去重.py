#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
# list2 = list(set(list1))
# print(list2)

list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


