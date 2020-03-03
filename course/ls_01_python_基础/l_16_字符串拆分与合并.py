poem_str = "登鹳雀楼\t \n 王之涣 \t白日依山尽"

# 拆分
poem_list = poem_str.split()
print(poem_list)

# 合并
resault =" ".join(poem_list)
print(resault)

# 切片
num_str = "0123456789"
print(num_str[-1: : -1])