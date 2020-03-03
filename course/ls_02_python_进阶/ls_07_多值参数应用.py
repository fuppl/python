def sum_nums(*args):
    """
    此函数可以计算任意个数和
    :param args: 要求和的任意个数
    :return: 和
    """
    resault = 0
    for i in args:
        resault += i
    return resault


def sum_nums2(args):
    """
    与上一个函数的区别在于，需要在传参时在外层加一对括号
    :param args: 要求和的任意个数
    :return: 和
    """
    resault = 0
    for i in args:
        resault += i
    return resault


print(sum_nums(1,2,3,4,5,6,7,8,9,11))
print(sum_nums2((1,2,3,4,5,6,7,8,9,11)))