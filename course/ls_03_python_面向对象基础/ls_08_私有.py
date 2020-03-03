class Women:

    def __init__(self, name, age):
        self.name = name
        # 实现私有通过在属性前加两个下划线"__"
        self.__age = age

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))

xiaomei = Women("小美", 18)
# 实现访问私有通过格式"_类名__属性/方法"
xiaomei._Women__secret()
