from settings import *
from pygame import *
import pygame

#Piece是方块类
#(x, y)是包围方块的矩形框的左上角在游戏区的坐标
#shape是方块代号，用作PIECES字典的键。
#turn是方块的翻转次数，决定方块的角度
#screen是窗口对象
class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.shape_template = PIECES[shape]
        self.turn = 0   #未翻转
        self.screen = screen

    def paint(self):
        shape_turn = self.shape_template[self.turn]
        #print(shape_turn)
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + WORK_AREA_LEFT + 1,
                         y * CELL_WIDTH + WORK_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, PIECE_COLORS[self.shape], cell_rect)

    def can_move_right(self):
        '''判断能否向右移动方块'''
        shape_turn = self.shape_template[self.turn]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    if self.x + c == COLUMN_NUM - 1:
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
        return True

    def move_left(self):
        if self.can_move_left():
            self.x -= 1

    def move_down(self):
        if self.can_move_down():
            self.y += 1

    def can_move_down(self):
        '''判断能否向左移动方块'''
        shape_turn = self.shape_template[self.turn]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    if self.y + r == LINE_NUM - 1:
                        return False   #方块已到达底部
        return True


    def turn_once(self):
        self.turn += 1
        if self.turn == len(self.shape_template):
            self.turn = 0