# list1 = []
# for i in range(10):
#     list1.append(i)
# print(list1)

# list1 = []
# i = 0
# while i < 10:
#     list1.append(i)
#     i += 1
# print(list1)

# list1 = [i for i in range(10)]
# print(list1)

# list1 = []
# for i in range(1, 3):
#     for j in range(3):
#         list1.append(i,j)
# print(i,j)

# dict1 = {i:i**2 for i in range(1,6)}
# print(dict1)

# list1 = ['name','age','gender']
# list2 = ['tom','20','man']
# dict1 = {list1[i]:list2[i] for i in range(len(list1))}
# print(dict1)
#
# counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
# counts1 = {key:value for key,value in counts.items() if value >= 200}
# print(counts1)

dict1 = {'lucy':21,'tom':30,'xiaoming':18,'xiaohong':15,'xiaowang':20,'xiaohei':19}
dict2 = {key:value for key,value in dict1.items()if value > 18}
print(dict2)