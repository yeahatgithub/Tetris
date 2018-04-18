# @Time    : 2018/4/17 17:07
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

from settings import *
import pygame

class GameDisplay():
    '''主程序的工具类。是绘制操作的集散地。'''

    @staticmethod
    def draw(screen, game_state):
        '''绘制游戏区域，即20*10的游戏区域'''
        GameDisplay.draw_border(screen, GAME_AREA_LEFT - EDGE_WIDTH, GAME_AREA_TOP, LINE_NUM, COLUMN_NUM)

        # 绘制未消掉方块组成的“墙”。
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_state.wall.area[r][c] != BLANK_LABEL:
                    GameDisplay.draw_cell(screen, c, r, PIECE_COLORS[game_state.wall.area[r][c]])

        GameDisplay.draw_score(screen, game_state.score)
        GameDisplay.draw_next_piece(screen, None)
        GameDisplay.draw_mannual(screen)
        if game_state.is_gameover:
            GameDisplay.draw_gameover(screen, game_state.session_count)  # 游戏结束！
        if game_state.is_paused:
            GameDisplay.draw_pause(screen)

    @staticmethod
    def draw_cell(screen, x, y, color):
        '''第y行x列的格子里填充color颜色。一种方块对应一种颜色。'''
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1,
                         y * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_score(screen, score):
        '''绘制游戏得分'''
        score_label_font = pygame.font.SysFont('stkaiti', 28)  # 换成'arial'，无法显示中文。

        # 添加下画线
        score_label_font.set_underline(True)
        score_label_surface = score_label_font.render(u'得分：', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH, GAME_AREA_TOP + 6 * CELL_WIDTH)
        screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 36)
        score_surface = score_font.render(str(score), False, (255, 0, 0))
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width + 20, score_label_position[1])
        screen.blit(score_surface, score_position)

    @staticmethod
    def draw_next_piece(screen, next_piece):
        '''绘制下一方块'''
        start_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH * 2
        start_y = GAME_AREA_TOP
        GameDisplay.draw_border(screen, start_x, start_y, 4, 4)

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        top_border = pygame.Rect(start_x, start_y, 2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, top_border)

        left_border = pygame.Rect(start_x, start_y, EDGE_WIDTH, 2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, left_border)

        right_border = pygame.Rect(start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y, EDGE_WIDTH,
                                   2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, right_border)

        bottom_border = pygame.Rect(start_x, start_y + EDGE_WIDTH + line_num * CELL_WIDTH,
                                    2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, bottom_border)


    @staticmethod
    def draw_gameover(screen, session_count):
        '''显示游戏结束'''
        gameover_font = pygame.font.SysFont('stkaiti', 36)
        gameover_surface = gameover_font.render(u'游戏结束', False, GAMEOVER_COLOR)
        gameover_position = (GAME_AREA_LEFT + 4 * CELL_WIDTH - CELL_WIDTH // 2, GAME_AREA_TOP + 10 * CELL_WIDTH)

        start_tip_surface = gameover_font.render(u'按s键开始新游戏', False, GAMEOVER_COLOR)
        start_tip_position = (GAME_AREA_LEFT + 2 * CELL_WIDTH, GAME_AREA_TOP + 11 * CELL_WIDTH)
        if session_count > 0:
            screen.blit(gameover_surface, gameover_position)
        screen.blit(start_tip_surface, start_tip_position)

    @staticmethod
    def draw_pause(screen):
        '''显示游戏暂停'''
        pause_font = pygame.font.SysFont('stkaiti', 36)
        pause_surface = pause_font.render(u'游戏暂停中', False, GAMEOVER_COLOR)
        pause_position = (GAME_AREA_LEFT + 3 * CELL_WIDTH, GAME_AREA_TOP + 10 * CELL_WIDTH)

        resume_tip_surface = pause_font.render(u'按p键继续', False, GAMEOVER_COLOR)
        resume_tip_position = (GAME_AREA_LEFT + 3 * CELL_WIDTH, GAME_AREA_TOP + 11 * CELL_WIDTH)
        screen.blit(pause_surface, pause_position)
        screen.blit(resume_tip_surface, resume_tip_position)

    @staticmethod
    def draw_mannual(screen):
        base_position_x = 40
        base_position_y = GAME_AREA_TOP + 40
        title_font = pygame.font.SysFont('stkaiti', 28)
        title_surface = title_font.render(u'玩法：', True, TITLE_COLOR)
        title_position = (base_position_x, base_position_y)
        screen.blit(title_surface, title_position)

        base_position_y += 60
        gamectrl_label_font = pygame.font.SysFont('stkaiti', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'全局控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'开始：s字母键；退出程序：e字母键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'暂停：p字母键；取消暂停：p字母键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'重新玩：r字母键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 60
        gamectrl_label_font = pygame.font.SysFont('stkaiti', 24)
        gamectrl_label_surface = gamectrl_label_font.render(u'方块控制', True, TITLE_COLOR)
        gamectrl_label_position = (base_position_x, base_position_y)
        screen.blit(gamectrl_label_surface, gamectrl_label_position)

        base_position_y += 40
        man_font = pygame.font.SysFont('stkaiti', 20)
        man_down_surface = man_font.render(u'翻转：上方向键；下移：下方向键', False, HANZI_COLOR)
        man_down_position = (base_position_x, base_position_y)
        screen.blit(man_down_surface, man_down_position)

        base_position_y += 40
        man_move_surface = man_font.render(u'左移：左方向键；右移：右方向键', False, HANZI_COLOR)
        man_move_position = (base_position_x, base_position_y)
        screen.blit(man_move_surface, man_move_position)

        base_position_y += 40
        man_speed_surface = man_font.render(u'快速到底：空格键或d字母键', False, HANZI_COLOR)
        man_speed_position = (base_position_x, base_position_y)
        screen.blit(man_speed_surface, man_speed_position)