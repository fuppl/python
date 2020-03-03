class Cat:

    def __init__(self,new_name):
        print("这是一只猫")
        self.name = new_name
    # __str__方法必须返回一个字符串
    def __str__(self):
        return "我是小猫[%s]" % self.name

tom = Cat("汤姆")
# 当定义__str__函数后，print(tom)将不在打印tom在内存中的地址，而是打印__str__中的内容
print(tom)