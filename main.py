import sys

import pygame
from pygame.locals import *
#各种配置
from settings import *
from Cell import Cell

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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")

    cell = Cell(screen)

    #游戏主循环
    while True:
        #事件处理
        check_events(cell)
        #设定屏幕背景色
        screen.fill(BG_COLOR)

        #绘制游戏区
        draw_workarea(screen)
        #绘制小方块
        cell.paint()

        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(cell):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            return on_key_down(event, cell)
        elif event.type == pygame.KEYUP:
            pass



def on_key_down(event, cell):
    if event.key == pygame.K_RIGHT:
        # print("按下了右箭头")
        cell.move_right()
    elif event.key == pygame.K_LEFT:
        # print("按下了左箭头")
        cell.move_left()


if __name__ == '__main__':
    main()
