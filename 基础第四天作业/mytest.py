#conding:utf-8

# list1 = ['1','2','3']
# list2 = []
# for i in list1:
#     i = int(i)
#     list2.append(i)
# print(list2)


# list1 = []
# list2 = []
# dict1 = {}
# f = open('data.txt','r',encoding='utf-8')
# content = f.readlines()
# f.close()
#
# for i in content:
#     i = i.strip('\n')
#     list1 = i.split('，')
#     for j in list1:
#         list2 = j.split(':')
#         # print(list2)
#         dict1[list2[0]] = int(list2[1])
# for key,value in dict1.items():
#     if value > 18:
#         print(f'{key}')

# str1 = 'welocme to super&Test'
# list3 = str1.split(' ')
# list4 = []
# for i in list3:
#     str2 = i[::-1]
#     list4.append(str2)
# print(' '.join(list4))

# str1 = 'welocme to super&Test'
# list1 = str1.split(' ')
# for i in list1:
#     list2 = i.split(',')
#     list3 = list(list2[0])
#
#     n = 0
#     while n < len(list3)/2:
#         tmp = list3[n]
#         list3[n] = list3[len(list3)-n-1]
#         list3[len(list3)-n-1] = tmp
#         n+=1
#     print(''.join(list3),end=' ')




















