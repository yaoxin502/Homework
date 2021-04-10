class Gun():
    def __init__(self,model,bullet_count):
        self.model = model
        self.bullet_count = bullet_count
    def shoot(self):
        if self.bullet_count == 0:
            print('请先装填子弹。')
        else:
            self.bullet_count -= 1
            print(f'射击成功,还剩{self.bullet_count}颗子弹。')
    def add_bullet(self,count):
        self.bullet_count += count
        print(f'已经装填了{count}颗子弹。')
    def __str__(self):
        return f'{self.model}有{self.bullet_count}颗子弹'

class Soldier():
    def __init__(self,name):
        self.name = name

    def fire(self,item):
        item.shoot()
        item.add_bullet(20)
    def __str__(self):
        return f'士兵{self.name}'

g1 = Gun('AK47',10)
s1 = Soldier('Ryan')
s1.fire(g1)
print(s1)
print(g1)