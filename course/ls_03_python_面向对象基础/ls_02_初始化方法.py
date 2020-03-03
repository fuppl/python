class Cat:

    # __init__是python 内置的初始化方法，在新建类时自动使用，无需调用
    # 在__init__中添加属性和默认值
    def __init__(self, new_name):
        print("这是一个初始化方法")
        # 如果不想使用默认值，可以传参
        # self.name = "lalal"
        # self.weight = 10
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


tom = Cat("汤姆")
tom.weight = 50
# tom.name = "tom"
print("猫的名字是 %s , 体重是 %d kg"%(tom.name, tom.weight))
tom.eat()