# 这是一个模拟新房子添置家具的过程

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.item_list = []
        self.free_area = area

    def __str__(self):
        return ("户型：%s\n总面积：%.2f [剩余面积：%.2f]\n家具名称列表 %s"
                %(self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        # 判断面积
        if item.area > self.free_area:
            print("家具[ %s ]占地面积太大，无法添加" % item.name)
            return
        self.item_list.append(item.name)
        self.free_area -= item.area


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地面积为 %.2f" % (self.name, self.area)


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

house = House("二层楼", 100)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)

print(house)
