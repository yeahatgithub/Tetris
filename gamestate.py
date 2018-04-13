# @Time    : 2018/4/13 9:50
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import random
from settings import *
from pieces import Piece
class GameState():
    def __init__(self, screen, game_area):
        #self.score = 0
        self.is_gameover = False
        self.screen = screen
        self.game_area = game_area
        self.piece = self.new_piece()

    def gameover(self):
        self.is_gameover = True

    def restart_game(self):
        self.is_gameover = False

    def new_piece(self):
        shape = random.randint(0, len(SHAPES) - 1)
        self.piece = Piece(SHAPES[shape], self.screen, self.game_area)
        return self.piece
