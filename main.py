import sys
import random
import pygame
#各种配置
from settings import *
from Cell import Cell
from pieces import Piece

def draw_workarea(screen):
    '''绘制游戏区域，即10X20的表格区域'''
    for r in range(21):
        pygame.draw.line(screen, EDEG_COLOR, (WORK_AREA_LEFT, WORK_AREA_TOP + r * CELL_WIDTH),
                         (WORK_AREA_LEFT + WORK_AREA_WIDTH, WORK_AREA_TOP + r * CELL_WIDTH))
    for c in range(11):
        pygame.draw.line(screen, EDEG_COLOR, (WORK_AREA_LEFT + c * CELL_WIDTH, WORK_AREA_TOP),
                         (WORK_AREA_LEFT + c * CELL_WIDTH, WORK_AREA_TOP + WORK_AREA_HEIGHT))


g_should_create_piece = True
def main():
    #初始化pygame
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(10, 100)  #一直按下某个键，每过100毫秒就引发一个KEYDOWN事件

    #cell = Cell(screen)
    # piece = Piece('S', screen)

    #游戏主循环
    while True:
        if g_should_create_piece:
            piece = create_piece(screen)

        #事件处理
        check_events(piece)

        #设定屏幕背景色.screen.fill()将刷新整个窗口。
        screen.fill(BG_COLOR)
        #绘制游戏区
        draw_workarea(screen)
        #刷新小方块
        #cell.paint()
        piece.paint()

        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(piece):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, piece)
        elif event.type == pygame.KEYUP:
            pass
            # on_key_up(event, piece)



def on_key_down(event, piece):
    if event.key == pygame.K_RIGHT:
        # print("按下了右箭头")
        piece.move_right()
    elif event.key == pygame.K_LEFT:
        # print("按下了左箭头")
        piece.move_left()
    elif event.key == pygame.K_DOWN:
        piece.move_down()
    elif event.key == pygame.K_UP:
        piece.turn_once()
    elif event.key == pygame.K_SPACE:
        piece.goto_bottom()
        global g_should_create_piece
        g_should_create_piece = True


def on_key_up(event, piece):
    if event.key == pygame.K_RIGHT:
        print("松开了右箭头")
    elif event.key == pygame.K_LEFT:
        print("松开了左箭头")

def create_piece(screen):
    shape = random.randint(0, len(SHAPES) - 1)
    p = Piece(SHAPES[shape], screen)
    global g_should_create_piece
    g_should_create_piece = False
    # print('create_piece()...')
    return p


if __name__ == '__main__':
    main()
