# 可以定义多值参数，*args接收列表，**kwargs接收字典
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="laosi", age=18)
