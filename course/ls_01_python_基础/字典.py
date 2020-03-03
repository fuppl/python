xiaoming = {"name": "xiaoming",
            "age": 22,
            "gender": True,
            "height": 1.75}

# 增
xiaoming["weight"] = 75
# 删
xiaoming.pop("weight")
# 改
xiaoming["name"] = "laosi"
# 查
print(xiaoming["name"])


# 统计键值对数量
print(len(xiaoming))
# 合并字典
# 如果被合并字典中含有已存在的键，则覆盖
temp_dict = {"lalal": 100}

xiaoming.update(temp_dict)
# 清空字典
# xiaoming.clear()

# 字典遍历
# k表示每次取得的key
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))

print(xiaoming)