# 当创建新对象时，python自动执行两个方法，__new__为变量提供空间并返回这个空间，
# __init__对变量进行初始化
class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 创建对象，new方法会被自动引用
        print("自动引用，分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)
        # 返回对象引用
        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)
