off_list = [[],[],[]]
tea_list = ['1','2','3','4','5','6','7','8']
import random
for i in tea_list:
    num = random.randint(0,2)
    off_list[num].append(i)
print(off_list)


