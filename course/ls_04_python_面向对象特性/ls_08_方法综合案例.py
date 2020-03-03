class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @classmethod
    def show_top_score(cls):
        print("游戏最高分为 %d" % cls.top_score)

    @staticmethod
    def show_help_information():
        print("假装我是帮助信息")

    def start_game(self):
        # todo 刷新最高分
        print("%s 开始游戏..." % self.player_name)

player1 = Game(input("请输入玩家姓名"))
player1.show_top_score()
Game.show_help_information()
player1.start_game()

