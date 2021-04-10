'''
有一堆字符串，“welocme to super&Test”，打印出emcolew ot  tseT&repus……全部单词原位置反转
'''
str1 = 'welocme to super&Test'
list1 = str1.split(' ')
for i in list1:
    list2 = i.split(',')
    list3 = list(list2[0])

    n = 0
    while n < len(list3)/2:
        tmp = list3[n]
        list3[n] = list3[len(list3)-n-1]
        list3[len(list3)-n-1] = tmp
        n+=1
    print(''.join(list3),end=' ')

