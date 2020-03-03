from ls_01_python_基础.ls_名片管理系统 import cards_tools

while True:

    cards_tools.show_menu()

    choice = input("请输入选项：")

    if choice == "1":
        cards_tools.new()
    elif choice == "2":
        cards_tools.show()
    elif choice == "3":
        name = input("想要查询的姓名：")
        cards_tools.seek(name)
    elif choice == "0":
        print("欢迎您再次使用")
        exit()
    else:
        print("出错，请重新选择")


