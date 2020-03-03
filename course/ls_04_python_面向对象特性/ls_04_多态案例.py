# 多态通过继承父类并重写父类方法实现不同类相同方法不同结果
# 为了与python2兼容，指明基类为object
class Dog(object):
    def __init__(self, name):
        self.name = name

    def play(self):
        print("%s 摇尾巴转圈" % self.name)


class Xiaotianquan(Dog):
    def __init__(self,name ):
        self.name = name

    def play(self):
        print("%s 想飞上天和太阳肩并肩" % self.name)

class Person:
    def __init__(self, name):
        self.name =name

    def play_with_dog(self,dog):
        print("%s 和 %s 玩" % (self.name, dog.name))
        dog.play()

wangcai = Dog("旺财")
xiaotian = Xiaotianquan("哮天犬")
# wangcai.play()
# xiaotian.play()
lilaosi = Person("李老四")
lilaosi.play_with_dog(wangcai)

