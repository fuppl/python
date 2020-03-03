# ddd
def multi():
    """输出九九乘法表"""
    col = 1
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            # \t表示垂直对齐
            print("%d * %d = %d" % (col, row, col*row), end="\t")
            col += 1
        print("")
        row += 1


def sum_2_num(num1, num2):
    """
    打印两数和
    :param num1: 加数
    :param num2: 加数
    :return: null
    """
    print("%d + %d = %d" % (num1, num2, num1 + num2))
