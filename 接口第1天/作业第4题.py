'''
4.士兵开枪
需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量
'''
'''
类1：士兵
属性：名字，枪名
方法：开火
类2：枪
属性：型号，子弹数
方法：发射子弹，装填子弹
'''
class Gun():
    def __init__(self,model,bullet_count):
        self.model = model
        self.bullet_count = bullet_count
    def shoot(self):
        if self.bullet_count == 0:
            print('请先装填子弹。')
        else:
            self.bullet_count -= 1
            print('射击成功。')
    def add_bullet(self,count):
        self.bullet_count += count
        print(f'已经装填了{count}颗子弹。')
    def __str__(self):
        return f'{self.model}有{self.bullet_count}颗子弹'

class Soldier():
    def __init__(self,name,gun_name):
        self.name = name
        self.gun_name = gun_name
    def fire(self):
        self.gun_name.shoot()
        self.gun_name.add_bullet(5)
    def __str__(self):
        return f'{self.name}有一把{self.gun_name}'

g1 = Gun('AK47',10)
s1 = Soldier('Ryan',g1)
s1.fire()
print(s1)
