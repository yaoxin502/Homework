class Gun():
    def __init__(self,name):
        self.name = name
        self.bullet_count = 0
    def __str__(self):
        return "制造一把%s有%d发子弹" % (self.name,self.bullet_count)
    def add_bullet(self):
        self.bullet_count += 20
        print('%d发子弹装填完毕'%self.bullet_count)
    def shot(self):
        self.bullet_count -= 1
        print('发射子弹1发，还剩%d发' % self.bullet_count)

class Soilder:
    def __init__(self,name):
        self.name = name
        # self.bullet = 0
    def __str__(self):
        return "士兵%s" % self.name
    def fire(self,item):
        if item.bullet_count > 0 :
            # print('%s子弹充足，进行射击' % item.name)
            print('士兵射击')
            item.shot()
        else:
            print('%s子弹不足，需要装填子弹' % item.name)
            item.add_bullet()

    def fun(self,a):
        print('a:',a)






AK = Gun("AK47")

print(AK.name)
print(AK.bullet_count)
AK.add_bullet()
AK.shot()


s = Soilder('瑞恩')
s.fire(AK)

b = 5

s.fun(b)
