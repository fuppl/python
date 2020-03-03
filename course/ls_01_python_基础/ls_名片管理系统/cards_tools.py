card_list = []


def show_menu():
    """
    显示功能菜单
    :return:
    """
    print("*" * 20)
    print("欢迎使用名片管理系统 v1.0")
    print("1.新建名片\n2.显示全部名片\n3.查询名片\n\n0.退出系统")
    print("*" * 20)


def new():
    """
    新建名片
    :return:
    """
    print("新建名片")
    card_dict = {"name": input("姓名："),
                 "phone": input("电话："),
                 "qq": input("qq："),
                 "email": input("邮箱：")}
    card_list.append(card_dict)
    print("添加成功")


def show():
    """
    显示全部名片
    :return:
    """
    print("显示全部")

    if len(card_list) == 0:
        print("没有名片，请新建")
        return

    # 打印表头与分割线
    for i in ["姓名", "电话", "QQ", "邮箱"]:
        print(i, end="\t\t")
    print("")
    print("-" * 30)

    for card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                        card["phone"],
                                        card["qq"],
                                        card["email"]))


def change(card_dict):
    """
    修改名片
    :param card_dict: 想要修改的名片字典
    :return:
    """
    card_dict["name"] = input_deal(card_dict["name"], "姓名")
    card_dict["phone"] = input_deal(card_dict["phone"], "电话")
    card_dict["qq"] = input_deal(card_dict["qq"], "QQ")
    card_dict["email"] = input_deal(card_dict["email"], "邮箱")


def remove(card_dict):
    """
    删除名片
    :param card_dict: 想要删除的名片
    :return:
    """
    card_list.remove(card_dict)
    print("删除名片成功")


def deal_with(card_dict):
    """
    执行查询后对名片的操作的选择，包括
    修改，删除，返回主菜单
    :param card_dict:
    :return:
    """
    choice = input("是否执行操作？（1.修改 / 2.删除 / 0.返回主菜单）:")
    if choice == "1":
        change(card_dict)
    elif choice == "2":
        remove(card_dict)
    else:
        return


def seek(Name):
    """
    查询名片xx
    :param Name:想要查询名片的名字
    :return:
    """
    print("查询名片")
    for card in card_list:
        if card["name"] == Name:
            print("找到 %s " % Name)
            for i in ["姓名", "电话", "QQ", "邮箱"]:
                print(i, end="\t\t")
            print("")
            print("-" * 30)
            print("%s\t\t%s\t\t%s\t\t%s" % (card["name"],
                                            card["phone"],
                                            card["qq"],
                                            card["email"]))
            deal_with(card)
            break
    else:
        print("没有找到 %s " % Name)


def input_deal(dict_value, tip_infornmation):
    """
    针对修改名片特制的输入函数
    :param dict_value: 想要修改的名片字典所原对应的值
    :param tip_infornmation: 名片字典键的名
    :return:如果用户输入了内容，返回用户输入的内容，否则返回原来的值
    """
    resault = input(tip_infornmation)

    if len(resault) == 0:
        return dict_value
    else:
        return resault
