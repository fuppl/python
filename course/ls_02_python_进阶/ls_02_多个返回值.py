def measure():
    print("测量开始...")
    # 温度
    temp = 39
    # 湿度
    wetness = 50
    print("测量结束")
    # 通过元组可以实现返回多个值
    # 元组的括号可以省略
    return temp, wetness


resault = measure()
print(resault)


# 若要单独使用温度或湿度需要使用索引，不方便
print(resault[0])
print(resault[1])


# ※※※※可以定义多个变量来接收元组类型返回值
gl_temp, gl_wetness = resault
print(gl_temp)
print(gl_wetness)