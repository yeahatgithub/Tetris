import sys
import pygame
from pygame.locals import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
COLUMN_NUM = 10
LINE_NUM = 20
WORK_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM
WORK_AREA_HEIGHT = CELL_WIDTH * LINE_NUM
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

    cell_position = (WORK_AREA_LEFT, WORK_AREA_TOP)

    #游戏主循环
    while True:
        #事件处理
        cell_position = check_events(cell_position)
        #print("main(), cell_position = ", cell_position)
        #设定屏幕背景色
        screen.fill(BG_COLOR)

        #绘制游戏区
        draw_workarea(screen)
        #绘制小方块
        draw_cell(screen, cell_position)

        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(cell_position):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #print("按下了右箭头")
                left, top = cell_position
                if left < WORK_AREA_LEFT + (COLUMN_NUM - 1) * CELL_WIDTH:
                    left = left + CELL_WIDTH  #向右移动一格
                return (left, top)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                #print("按下了左箭头")
                left, top = cell_position
                if left > WORK_AREA_LEFT:
                    left = left - CELL_WIDTH  # 向右移动一格
                return (left, top)

    return  cell_position


def draw_cell(screen, cell_position):
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)
    cell_rect = Rect(cell_position, cell_width_height)
    pygame.draw.rect(screen, CELL_COLOR, cell_rect)


if __name__ == '__main__':
    main()
