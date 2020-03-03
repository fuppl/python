class Person:
    def __init__(self, new_name, new_weight):
        self.name = new_name
        self.weight = new_weight

    def __str__(self):
        return " %s 的体重是 %.1f kg" % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


xiaoming = Person("小明", 75)

xiaoming.run()
xiaoming.run()
xiaoming.eat()
xiaoming.run()

print(xiaoming.__str__())