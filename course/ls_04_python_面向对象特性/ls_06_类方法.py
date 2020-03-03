# 把类看做一个对象，类也可以有自己的属性和方法
class Tool:
    count = 0
    name = "Tool类"
    # 可以统计有多少个子类
    def __init__(self):
        Tool.count += 1


    # 定义类方法需要，需要在上面标注@classmethod,参数为cls,是class的缩写，作用与self类似，不用传参
    @classmethod
    def show_tools_count(cls):
        print("%s 有 %d 个" %(cls.name, cls.count))


lala = Tool()
# print(Tool.count)
abc = Tool()
# print(Tool.count)
Tool.show_tools_count()