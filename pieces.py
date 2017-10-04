from settings import *
from pygame import *
import pygame

class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.turn = 0   #翻转了几次，决定显示的模样
        self.screen = screen

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn]
        #print(shape_turn)
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + WORK_AREA_LEFT,
                         y * CELL_WIDTH + WORK_AREA_TOP)
        cell_width_height = (CELL_WIDTH, CELL_WIDTH)
        cell_rect = Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)

    def move_right(self):
        if self.x < (COLUMN_NUM - 1):
            self.x = self.x + 1  # 向右移动一格

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_down(self):
        if self.y < (LINE_NUM - 1):
            self.y += 1