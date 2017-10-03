import sys
import pygame

def main():
    #初始化pygame
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((1200, 800) )
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
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    main()