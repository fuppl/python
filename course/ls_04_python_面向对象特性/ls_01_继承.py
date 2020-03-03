# 继承格式 class 子类名（父类名）：
class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class Xiaotianquan(Dog):
    def fly(self):
        print("飞")
    # 方法重写直接 def 父类方法的名字即可
    def bark(self):
        print("嗷嗷叫")
        # 可以使用super在重写方法的过程中调用父类的方法
        super().bark()
        print("lalal")


wangcai = Dog()
wangcai.bark()
zhonghuadiwangquan = Xiaotianquan()
zhonghuadiwangquan.fly()
zhonghuadiwangquan.bark()

