while True:
# 接收一个整数，并用8除以这个整数
    try:
        num = int(input("输入一个整数"))
        print(8/num)
    except ZeroDivisionError:
        print("除数不能为0")
    except ValueError:
        print("请输入整数")

    # todo 捕获未知错误
    except Exception as resault:
        print("未知错误%s" % resault)
