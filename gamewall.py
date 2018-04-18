# @Time    : 2018/4/3 14:40
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT
# import pygame
from settings import *


'''
游戏区有20*10个单元格。
最开始，每一个单元格填充了BLANK_LABEL。
此后，随着方块落到底部，一个单元格可能填充'SZJLOIT'等字母，表明该单元格曾被相应形状的方块占据。
'''

class GameWall():
    '''游戏区类。记住落到底部，且未被消掉的方块组成的“墙”。'''
    def __init__(self, screen):
        '''游戏开始时，游戏区20*10个格子被'-'符号填充。“墙”是空的。'''
        self.screen = screen
        self.area = []
        line = [BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])
        # self.desc()
        #self.score = 0

    def desc(self):
        '''打印20*10的二维矩阵self.area的元素值。用于调试。'''
        print(len(self.area), "rows", len(self.area[0]), "colums")
        for line in self.area:
            print(line)


    def set_cell(self, position, shape_label):
        '''把第r行c列的格子打上方块记号（如S, L...），因为该格子被此方块占据。'''
        c, r = position
        self.area[r][c] = shape_label
        # self.desc()

    def is_wall(self, r, c):
        return self.area[r][c] != BLANK_LABEL

    def eliminate_lines(self):
        '''消行。如果一行没有空白单元格，就消掉该行。返回得分。'''
        lines_eliminated = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                lines_eliminated.append(r)

        #刷新游戏区，消行
        for r in lines_eliminated:
            self.copy_down(r)
            for c in range(COLUMN_NUM):
                self.area[0][c] = BLANK_LABEL

        return len(lines_eliminated)


    def is_full(self, line_no):
        '''line_no行满了吗'''
        for c in range(COLUMN_NUM):
            if self.area[line_no][c] == BLANK_LABEL:
                return False

        return True


    def copy_down(self, line_no):
        '''把line_no上面各行下沉一行。'''
        for r in range(line_no, 0, -1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r - 1][c]

    def clear(self):
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                self.area[r][c] = BLANK_LABEL


