# 异常的传递性指发生异常时程序不会直接终止，
# 而是把异常交给调用发生异常函数，一级一级传递，
# 直到主程序没有处理异常，程序才会报错，
# 可以利用异常的传递性，在主程序处理异常
def demo():
    return int(input("输入整数"))

try:
    demo()
except Exception as resault:
    print("未知错误%s" % resault)