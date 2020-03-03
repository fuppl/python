# 题目要求，不使用其他变量，交换两个变量的值
def method1(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


# 方法2python专享
def method2(a, b):
    a, b = b, a
    return a, b