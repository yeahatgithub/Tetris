import sys
import pygame

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
WORK_AREA_WIDTH = CELL_WIDTH * 10
WORK_AREA_HEIGHT = CELL_WIDTH * 20
WORK_AREA_LEFT = (SCREEN_WIDTH - WORK_AREA_WIDTH) // 2
WORK_AREA_TOP = SCREEN_HEIGHT - WORK_AREA_HEIGHT
EDEG_COLOR = (0, 0, 0)

def drawWorkArea(screen):
    #pygame.draw.line(screen, (0, 0, 0), (100, 100), (200, 200))
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

    #屏幕背景色
    bg_color = (230, 230, 230)

    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #设定屏幕背景色
        screen.fill(bg_color)

        drawWorkArea(screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    main()
