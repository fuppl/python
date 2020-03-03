# 分割线函数
def print_line(char, times, line):
    """
打印多行分割线

    :param char: 分割线使用的字符
    :param times: 字符重复的次数
    :param line: 分割线行数
    """
    i = 0
    while i < line:
        print(char * times)
        i += 1


print_line("* ", 5, 5)
