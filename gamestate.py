# @Time    : 2018/4/13 9:50
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import random
from settings import *
from pieces import Piece
import pygame
class GameState():
    def __init__(self, screen, game_area):
        #self.score = 0
        self.is_gameover = True   #按s键开始游戏
        self.is_paused = False
        self.screen = screen
        self.game_area = game_area
        self.piece = self.new_piece()
        self.score = 0
        self.timer_interval = 1000   #1000ms
        self.session_count = 0   #玩第几轮？

    def gameover(self):
        self.is_gameover = True

    def restart_game(self):
        self.is_gameover = False
        self.set_timer(self.timer_interval)
        self.session_count += 1

    def pause_game(self):
        self.remove_timer()
        self.is_paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.is_paused = False

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def remove_timer(self):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, 0)

    def new_piece(self):
        shape = random.randint(0, len(SHAPES) - 1)
        self.piece = Piece(SHAPES[shape], self.screen, self.game_area)
        return self.piece

    def add_score(self, eliminated_line_num):
        '''消行计分'''
        '''
        计分规则：
        消掉1行：100分
        消掉2行：200分
        消掉3行：400分
        消掉4行：800分
        '''
        assert(eliminated_line_num <= 4 and eliminated_line_num >= 0)
        if eliminated_line_num < 3:
            self.score += eliminated_line_num * 100
        elif eliminated_line_num == 3:
            self.score += 400
        else:
            self.score += 800