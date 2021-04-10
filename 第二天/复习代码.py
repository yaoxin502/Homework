# mystr = "hello world and superctest and chaoge and Python"
# print(mystr.find('and'))
# print(mystr.find('and',15,30))
# print(mystr.find('ands'))

# print(mystr.index('ands'))

# print(mystr.count('and'))
# print(mystr.count('ands'))

# print(mystr.replace('and','or',1))
# print(mystr.split('and',1))
# print('.'.join(mystr))
# print(mystr.capitalize())
# print(mystr.title())
# print(mystr.lower())
# print(mystr.upper())

# print(mystr.lstrip())
# print(mystr.rstrip())
# print(mystr.strip())

# print(mystr.ljust(50,'.'))
# print(mystr.rjust(50,'.'))
# print(mystr.center(50,'.'))

# print(mystr.startswith('hello'))
# print(mystr.endswith('and'))
# str1 = 'hello123'
# print(str1.isalpha())
# print(str1.isdigit())
# print(str1.isalnum())
# print(str1.isspace())

# name_list = ['Tom', 'Lily', 'Rose','Rose']
# print(name_list.index('tom'))
# print(name_list.count('Rose'))
# print(len(name_list))
# print('Lily'in name_list)
# print('lily'not in name_list)

# name_list.append('xiaohua100')
# name_list.extend('xiaohua')
# name_list.insert(1,'xiaohua')
# del name_list
# del name_list[3]
# del_name = name_list.pop(1)
# print(del_name)
# name_list.remove('Tom')
# name_list.clear()
# name_list[3]='xiaohua'
# name_list.reverse()
# list1 = [5,3,7,4,9]
# list1.sort(reverse=True)
# list2 = list1.copy()
# print(list2)

# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1

# for i in name_list:
#     print(i)

# import random
# list1 = [[],[],[]]
# list2 = ['1','2','3','4','5','6','7','8']
# for i in list2:
#     num = random.randint(0,2)
#     list1[num].append(i)
# print(list1)

# t1 = ('hello',)
# print(type(t1))

# tuple1 = ('aa', 'bb', 'cc', 'bb')
# print(tuple1[0])
# print(tuple1.index('dd'))
# print(tuple1.count('bb'))
# print(len(tuple1))
# tuple1[0]='aaa'

# dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict1['id'] = 110
# del dict1['name']
# dict1.clear()
# del dict1
# print(dict1.get('id',110))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# for i in dict1.keys():
#     print(i)
# for j in dict1.values():
#     print(j)
# for a,b in dict1.items():
#     print(f'{a}:{b}')

# set1 = {1,2,3,4,5}
# set1.add(3)
# set1.update([2,3])
# set1.discard(10)
# del_num = set1.pop()
# print(del_num)
# print(set1)

# print('-'* 10)
# list1 = ['hello']
# print(list1 * 4)

# t1 = (1,2,3,4)
# for i,j in enumerate(t1,start=1):
#     print(f'下标是{i}，对应字符是{j}')

# list1 = [i for i in range(10) if i % 2 == 0]
# print(list1)

# list1 = []
# for i in range(1,3):
#     for j in range(3):
#         list1.append((i,j))
# print(list1)

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
count1 = {key:value for key,value in counts.items() if value >= 200}
print(count1)