# @Time    : 2018/4/19 11:03
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
class GameImages():
    def __init__(self):
        self.gameover_img = None
        self.pausing_img = None
        self.continue_img = None
        self.newgame_img = None
        self.path = 'images/'

    def load_gameover_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(self.path + "game-over.png").convert_alpha()

        return self.gameover_img

    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.path + "press-s-newgame.png").convert_alpha()

        return self.newgame_img

    def load_pausing_img(self):
        if not self.pausing_img:
            self.pausing_img = pygame.image.load(self.path + "game-pausing.png").convert_alpha()
        return self.pausing_img

    def load_continue_img(self):
        if not self.continue_img:
            self.continue_img = pygame.image.load(self.path + "press-p-continue.png").convert_alpha()

        return self.continue_img