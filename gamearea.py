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

class GameArea():
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

    def draw(self, score):
        '''绘制游戏区域，即20*10的游戏区域'''
        for r in range(LINE_NUM + 1):
            pygame.draw.line(self.screen, EDEG_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
                             (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
        for c in range(COLUMN_NUM + 1):
            pygame.draw.line(self.screen, EDEG_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
                             (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

        #绘制未消掉方块组成的“墙”。
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if self.area[r][c] != BLANK_LABEL:
                    self.draw_cell(c, r, PIECE_COLORS[self.area[r][c]])

        self.draw_score(score)
        self.draw_mannual()

    def draw_cell(self, x, y, color):
        '''第y行x列的格子里填充color颜色。一种方块对应一种颜色。'''
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1,
                         y * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, color, cell_rect)

    def draw_score(self, score):
        '''绘制游戏得分'''
        score_label_font = pygame.font.SysFont('stkaiti', 28)   #换成'arial'，无法显示中文。

        # 添加下画线
        score_label_font.set_underline(True)
        score_label_surface = score_label_font.render(u'得分：', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 40, GAME_AREA_TOP)
        self.screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(score), False, (255, 0, 0))
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] +score_label_width + 20, score_label_position[1])
        self.screen.blit(score_surface, score_position)

    def draw_gameover(self):
        '''显示游戏结束'''
        gameover_font = pygame.font.SysFont('stkaiti', 36)
        gameover_surface = gameover_font.render(u'游戏结束', False, GAMEOVER_COLOR)
        gameover_position = (GAME_AREA_LEFT + 150, GAME_AREA_TOP + 400)
        self.screen.blit(gameover_surface, gameover_position)

    def draw_mannual(self):
        base_position_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 40
        base_position_y = GAME_AREA_TOP + 400
        man_font = pygame.font.SysFont('stkaiti', 18)
        title_surface = man_font.render(u'玩法：', False, HANZI_COLOR)
        title_position = (base_position_x, base_position_y)
        self.screen.blit(title_surface, title_position)

        man_down_surface = man_font.render(u'翻转：上方向键；下移：下方向键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y + 60)
        self.screen.blit(man_down_surface, man_down_position)

        man_move_surface = man_font.render(u'左移：左方向键；右移：右方向键', False, HANZI_COLOR)
        man_move_position = (base_position_x, base_position_y + 120)
        self.screen.blit(man_move_surface, man_move_position)


        man_speed_surface = man_font.render(u'快速到底：空格键或d字母键', False, HANZI_COLOR)
        man_speed_position = (base_position_x, base_position_y + 180)
        self.screen.blit(man_speed_surface, man_speed_position)

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


