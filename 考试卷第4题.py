'''
4.文件data.txt内存在以下内容（每行采用逗号分隔）（15分）
lucy:21，tom:30
xiaoming:18，xiaohong:15
xiaowang:20，xiaohei:19
输出年龄大于18岁的人名
'''
list1 = []
list2 = []
dict1 = {}
f = open('data.txt','r',encoding='utf-8')
content = f.readlines()
f.close()

for i in content:
    i = i.strip('\n')
    list1 = i.split('，')
    for j in list1:
        list2 = j.split(':')
        # print(list2)
        dict1[list2[0]] = int(list2[1])
for key,value in dict1.items():
    if value > 18:
        print(f'{key}')


