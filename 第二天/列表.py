# name_list = ['tom','lily','rose','tom']
# print(name_list.index('lily'))
# print(name_list.count('tom'))
# print(len(name_list))
# print('rose' in name_list)

# name_list = ['zhangsan','lisi','wangwu']
# name = input('输入姓名：')
# if name in name_list:
#     print(f'您输入的名字是{name}，名字存在')
# else:
#     print('名字不存在')

# name_list = ['tom','lily','rose']
# name_list.append(['xiaoming','xiaohong'])
# name_list.extend('xiaoming')
# print(name_list)

# name_list = ['Tom', 'Lily', 'Rose']
# # del name_list[0]
# # del_name = name_list.pop(1)
# name_list.clear()
# print(name_list)

# name_list = ['Tom', 'Lily', 'Rose']
# name_list[1] = 'xiaoming'
# print(name_list)

# num_list = [1,3,5,6,8,7]
# # num_list.reverse()
# num_list.sort(reverse=True)
# print(num_list)
# num_list1 = num_list.copy()
# print(num_list1)

name_list = ['tom','lily','rose']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
    
name_list1 = ['tom','lily','rose']
for i in name_list1:
    print(i)