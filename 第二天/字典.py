# dict1 = {'name':'tom','age':'20','gender':'男'}
# dict1['name'] = 'rose'
# # dict1['id'] = 110
# # del dict1['age']
# # # dict1.clear()
# # print(dict1)
# # print(dict1['name'])
# # print(dict1.get('age',18))
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())


dict1 = {'name':'tom','age':'20','gender':'男'}
# for key in dict1.keys():
#     print(key)
#
# for v in dict1.values():
#     print(v)

# for i in dict1.items():
#     print(i)

for k,v in dict1.items():
    print(f'{k} = {v}')