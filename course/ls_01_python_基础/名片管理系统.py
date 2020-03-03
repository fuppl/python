# 新建
def new():
    card_dict = {"name": input("姓名："),
                 "phone": input("电话："),
                 "qq": input("qq："),
                 "email": input("邮箱：")}
    card_list.append(card_dict)

# 显示全部
def show():
    for card in card_list:
        print(card)


def change(Name):
    for card in card_list:
        if card[0] == Name:
            card1 = card
            break

    choice = input("想要修改的内容(name/phone/qq/email)")
    for c in card1:
        if c == choice:


def remove(Name):

# 查询，包含修改与删除
def seek(Name):

    for card in card_list:
        if card[0] == Name:
            print("找到%s" % Name)
            option = input("是否执行操作？(0否1是)：")
            break
    else:
        print("没有找到%s" % Name)

    if option ==1:
        choice = input("1.修改\t2.删除")
        if choice == 1:
            change(Name)
        elif choice == 2:
            remove(Name)
        else:
            print("出错")


print("*" * 20)
print("欢迎使用名片管理系统 v1.0")
print("1.新建名片\t2.显示全部名片\t3.查询名片\t\t0.退出系统\t")
print("*"* 20)
choice = int(input("请输入选项："))
card_list = []

if choice == 1:
    new()
elif choice ==2:
    show()
elif choice ==3:
    name = input("想要查询的姓名：")
    seek(name)
else:
    exit()


