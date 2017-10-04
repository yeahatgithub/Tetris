from settings import *
from pygame.locals import *
import pygame


class Cell():
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        # self.moving_right = False
        # self.moving_left = False
        self.screen = screen

    def move_right(self):
        if self.x < (COLUMN_NUM - 1):
            self.x = self.x + 1  # 向右移动一格

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def paint(self):
        cell_position = (self.x * CELL_WIDTH + WORK_AREA_LEFT,
                         self.y * CELL_WIDTH + WORK_AREA_TOP)
        cell_width_height = (CELL_WIDTH, CELL_WIDTH)
        cell_rect = Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y