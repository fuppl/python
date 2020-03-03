# 单例表示所有用这个类创建的对象都是同一个对象，可用地址验证
class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        """
        实现单例，创建时判断是否曾经创建过对象，有就返回曾经创建的对象
        :param args:
        :param kwargs:
        :return:
        """
        if cls.instance == None:
            # todo __new__()里必须添上cls，否则出错
            cls.instance = super().__new__(cls)
            return cls.instance
        else:
            return cls.instance

    # 新建几次，执行几次,
    # 可以用flag使init只执行一次
    @classmethod
    def __init__(self):
        if MusicPlayer.init_flag==False:
            print("初始化播放器")

        else:
            return

        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

