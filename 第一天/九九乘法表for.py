'''
本题需要两个循环控制，分别是行和列
i是行，j是列
i是外循环，j是内循环
'''
for i in range(1,10):
    for j in range(1,i+1):
        sum = j * i
        print(f'{j}*{i}={sum}',end=' ')
    print()
