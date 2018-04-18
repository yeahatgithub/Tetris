from settings import *
import pygame

#Piece是方块类
#(x, y)是包围方块的矩形框的左上角在游戏区的坐标
#shape是方块代号，用作PIECES字典的键。
#turn是方块的翻转次数，决定方块的角度
#screen是窗口对象
from game_display import GameDisplay

class Piece():
    def __init__(self, shape, screen, game_area):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.shape_template = PIECES[shape]
        self.turn = 0   #未翻转
        self.screen = screen
        self.game_area = game_area

    def paint(self):
        shape_turn = self.shape_template[self.turn]
        #print(shape_turn)
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        GameDisplay.draw_cell(self.screen, x, y, PIECE_COLORS[self.shape])

    def can_move_right(self):
        '''判断能否向右移动方块'''
        shape_turn = self.shape_template[self.turn]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    if self.x + c == COLUMN_NUM - 1:
                        return False
                    elif self.game_area.is_wall(self.y + r, self.x + c + 1):
                        return False
        return True

    def move_right(self):
        if self.can_move_right():
            self.x = self.x + 1  # 向右移动一格

    def can_move_left(self):
        '''判断能否向左移动方块'''
        shape_turn = self.shape_template[self.turn]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    if self.x + c == 0:
                        return False
                    elif self.game_area.is_wall(self.y + r, self.x + c - 1):
                        return False
        return True

    def can_move_down(self):
        '''判断能否向下移动方块'''
        shape_turn = self.shape_template[self.turn]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    if self.y + r == LINE_NUM - 1:
                        return False   #方块已到达底部
                    elif self.game_area.is_wall(self.y + r + 1, self.x + c):
                        return False
        return True

    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        '''如果到底了，返回True值，表示已经到底了，否则返回False。'''
        if self.can_move_down():
            self.y += 1
            return False
        else:
            self.insert_into_wall()
            return True

    def turn_once(self):
        turn = self.turn
        turn += 1
        if turn == len(self.shape_template):
            turn = 0
        if self.can_turn(self.shape_template[turn]):
            self.turn = turn


    def can_turn(self, shape_turn):
        row_num = len(shape_turn)
        col_num = len(shape_turn[0])
        for r in range(row_num):
            for c in range(col_num):
                if shape_turn[r][c] == 'O' :
                    # print("row:", r + self.y, "column:", c + self.x)
                    if c + self.x < 0 or c + self.x >= COLUMN_NUM or r + self.y < 0 or r + self.y >= LINE_NUM:
                        return False   #出界
                    if self.game_area.is_wall(r + self.y, c + self.x):
                        return False
        return True

    def goto_bottom(self):
        '''直接坠落到底部'''
        '''这里，底部是指按游戏规则再也无法往下移动的位置。'''
        while self.can_move_down():
            self.y += 1
        self.insert_into_wall()


    def insert_into_wall(self):
        shape_turn = self.shape_template[self.turn]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.game_area.set_cell((self.x + c, self.y + r), self.shape)