def demo1(num):
    print("demo1内部")
    num += num
    print(num)
    print("demo1结束")


def demo2(num):
    print("demo2内部")
    num = num + num
    print(num)
    print("demo2结束")


# 数字的+=表示相加再赋值，使用赋值语句，实参不变；而列表的+=实际上是调用列表的extend函数，实参改变
# 若改为demo2，则列表不变
num = 9
num_list = [1, 2, 3]

demo1(num)
print(num)

demo2(num_list)
print(num_list)

demo1(num_list)
print(num_list)
