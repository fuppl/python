# 把类看做一个对象，类也可以有自己的属性和方法
class Tool:
    count = 0
    # 可以统计有多少个子类
    def __init__(self):
        Tool.count += 1


lala = Tool()
print(Tool.count)
abc = Tool()
print(Tool.count)