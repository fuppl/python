class Cat:
    # 哪一个对象调用，self表示哪一个对象
    # 定义方法时，第一个参数一定是self，否则无法调用
    
    def drink(self):
        print("%s要喝水" % self.name)
    def eat(self):
        print("%s爱吃鱼" % self.name)



tom = Cat()
tom.name = "tom"
tom.eat()
tom.drink()

