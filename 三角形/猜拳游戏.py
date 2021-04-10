#电脑生成随机数
import random
com = random.randint(1,3)
print(com)

p = int(input('玩家出拳（剪刀-1，石头-2，布-3）：'))
if ((p == 1 and com == 3)or(p == 2 and com == 1)or(p == 3 and com ==2)):
    print('玩家赢')
elif (p == com):
    print('平局')
else:
    print('玩家输')