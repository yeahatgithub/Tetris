# @Time    : 2018/4/13 9:50
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
class GameState():
    def __init__(self, screen):
        self.is_gameover = True   #按s键开始游戏
        self.is_paused = False
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.next_piece = None
        self.score = 0
        self.timer_interval = TIMER_INTERVAL   #1000ms
        self.session_count = 0   #玩第几轮？


    def gameover(self):
        self.is_gameover = True

    def start_game(self):
        self.is_gameover = False
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        self.session_count += 1
        self.new_piece()   #此时, self.piece = None
        self.new_piece()   #此时，self.piece, self.next_piece都不等于None
        self.score = 0

    def restart_game(self):
        self.wall.clear()
        self.start_game()


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
        self.piece = self.next_piece
        self.next_piece = Piece(SHAPES[shape], self.screen, self.wall)
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

    def touch_bottom(self):
        '''方块落到底部时，要消行，要生成新方块。如果触到顶部，游戏终止。'''
        self.add_score(self.wall.eliminate_lines())
        for c in range(COLUMN_NUM):
            if self.wall.is_wall(0, c):
                # game_area.draw_gameover()   #在这里绘制文字是不起作用的。必须放到主循环中。
                # print("game over!")
                self.gameover()
                break
        if not self.is_gameover:
            self.new_piece()