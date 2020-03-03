num = 10


def num1():
    # global表示全局变量的声明
    global num
    num = 50
    print("num1 num = %d" % num)


def num2():
    print("num2 num = %d" % num)


num1()
num2()
