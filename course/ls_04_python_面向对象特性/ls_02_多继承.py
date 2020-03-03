class A:
    def test(self):
        print("A类test方法")


class B:
    def demo(self):
        print("B类demo方法")


class C(A, B):
    pass


c = C()
c.test()
c.demo()