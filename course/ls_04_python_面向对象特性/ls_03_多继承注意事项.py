class A:
    def test(self):
        print("A类test方法")
    def demo(self):
        print("A类demo方法")

class B:
    def demo(self):
        print("B类demo方法")
    def test(self):
        print("B类test方法")

class C(A, B):
    pass

class D(B, A):
    pass

# 一旦父类的方法名相同，按多继承的父类排序顺序
c = C()
c.test()
c.demo()
d = D()
d.test()
d.demo()