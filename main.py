import sys
import pygame
from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
WORK_AREA_WIDTH = CELL_WIDTH * 10
WORK_AREA_HEIGHT = CELL_WIDTH * 20
WORK_AREA_LEFT = (SCREEN_WIDTH - WORK_AREA_WIDTH) // 2
WORK_AREA_TOP = SCREEN_HEIGHT - WORK_AREA_HEIGHT
EDEG_COLOR = (0, 0, 0)
CELL_COLOR = (100, 100, 100)
BG_COLOR = (230, 230, 230)

def draw_workarea(screen):
    '''绘制游戏区域，即10X20的表格区域'''
    for r in range(21):
        pygame.draw.line(screen, EDEG_COLOR, (WORK_AREA_LEFT, WORK_AREA_TOP + r * CELL_WIDTH),
                         (WORK_AREA_LEFT + WORK_AREA_WIDTH, WORK_AREA_TOP + r * CELL_WIDTH))
    for c in range(11):
        pygame.draw.line(screen, EDEG_COLOR, (WORK_AREA_LEFT + c * CELL_WIDTH, WORK_AREA_TOP),
                         (WORK_AREA_LEFT + c * CELL_WIDTH, WORK_AREA_TOP + WORK_AREA_HEIGHT))


def main():
    #初始化pygame
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT) )
    pygame.display.set_caption("俄罗斯方块")

    #游戏主循环
    while True:
        #事件处理
        check_events()
        #设定屏幕背景色
        screen.fill(BG_COLOR)

        #绘制游戏区
        draw_workarea(screen)
        #绘制小方块
        draw_cell(screen, WORK_AREA_LEFT, WORK_AREA_TOP)

        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events():
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("方块向右移动")
                pass
        elif event.type == pygame.KEYUP:
            pass


def draw_cell(screen, left, top):
    cell_left_top = (left, top)
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)
    cellRect = Rect(cell_left_top, cell_width_height)
    pygame.draw.rect(screen, CELL_COLOR, cellRect)


if __name__ == '__main__':
    main()
