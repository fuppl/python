class Gun:
    def __init__(self, bullet_num):
        self.bullet_num = bullet_num

    def add_bullet(self):
        self.bullet_num += 30
        print("装蛋完成")

    def shoot(self):
        if self.bullet_num <=0:
            self.add_bullet()
        self.bullet_num -= 3

    def __str__(self):
        return "子弹还剩 %d 颗" % self.bullet_num


class Solider:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def fire(self):
        self.gun.shoot()

    def __str__(self):
        return "士兵 %s 还剩 %d 颗子弹" %(self.name, self.gun.bullet_num)


AK47 = Gun(360)
xusanduo = Solider("xusanduo", AK47)

xusanduo.fire()
xusanduo.fire()
xusanduo.fire()
print(AK47)
print(xusanduo)
