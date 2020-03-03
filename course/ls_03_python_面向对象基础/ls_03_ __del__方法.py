class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("%s来了" % self.name)

    def __del__(self):
        print("%s走了" % self.name)


tom = Cat("tom")
print("-"* 50)

lazy_cat = Cat("大懒猫")
del lazy_cat
print("-"* 50)
