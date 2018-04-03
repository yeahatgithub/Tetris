# @Time    : 2018/4/3 14:40
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
import pygame
from settings import *
BLANK_LABEL = '-'
'''
游戏区有20*10个单元格。
最开始，每一个单元格填充了BLANK_LABEL。
此后，随着方块落到底部，一个单元格可能填充'SZJLOIT'等字母，表明该单元格曾被相应形状的方块占据。
'''

class WorkArea():
    '''游戏区'''
    def __init__(self, screen):
        self.screen = screen
        self.wall = []
        line = [BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.wall.append(line[:])

    def draw(self):
        '''绘制游戏区域，即10X20的表格区域'''
        for r in range(21):
            pygame.draw.line(self.screen, EDEG_COLOR, (WORK_AREA_LEFT, WORK_AREA_TOP + r * CELL_WIDTH),
                             (WORK_AREA_LEFT + WORK_AREA_WIDTH, WORK_AREA_TOP + r * CELL_WIDTH))
        for c in range(11):
            pygame.draw.line(self.screen, EDEG_COLOR, (WORK_AREA_LEFT + c * CELL_WIDTH, WORK_AREA_TOP),
                             (WORK_AREA_LEFT + c * CELL_WIDTH, WORK_AREA_TOP + WORK_AREA_HEIGHT))