def input_password():
    password = input("请输入密码")
    if len(password) < 8:
        # TODO 创建异常，括号内可输入提示信息
        ex = Exception("密码长度不够")
        # TODO 主动抛出异常
        raise ex
    else:
        return password


try:
    print(input_password())
except Exception as resault:
    print(resault)