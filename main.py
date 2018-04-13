import sys
import random
import pygame
#各种配置
from settings import *
from pieces import Piece
from gamearea import GameArea
from gamestate import GameState

def draw_workarea(screen):
    '''绘制游戏区域，即10X20的表格区域'''
    for r in range(21):
        pygame.draw.line(screen, EDEG_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
    for c in range(11):
        pygame.draw.line(screen, EDEG_COLOR, (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))


def main():
    #初始化pygame
    pygame.init()
    #创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(10, 100)  #一直按下某个键，每过100毫秒就引发一个KEYDOWN事件

    game_area = GameArea(screen)
    # print(pygame.font.get_fonts())
    game_state = GameState(screen, game_area)
    # piece = game_state.piece
    game_timer = pygame.time.set_timer(pygame.USEREVENT, game_area.timer_interval)
    #游戏主循环
    while True:
        #事件处理
        check_events(game_area, game_state)

        #设定屏幕背景色.screen.fill()将刷新整个窗口。
        screen.fill(BG_COLOR)
        #绘制游戏区
        game_area.draw(game_state.score)

        if game_state.is_gameover:
            game_area.draw_gameover()   #游戏结束！
            #print("game over!")

        #更新方块
        game_state.piece.paint()

        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(game_area, game_state):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_area, game_state)
        elif event.type == pygame.KEYUP:
            pass
            # on_key_up(event, piece)
        elif event.type == pygame.USEREVENT:
            reached_bottom = game_state.piece.move_down()
            if reached_bottom:
                touch_bottom(game_area, game_state)

    #return game_state.piece



def on_key_down(event, game_area, game_state):
    if event.key == pygame.K_RIGHT:
        # print("按下了右箭头")
        game_state.piece.move_right()
    elif event.key == pygame.K_LEFT:
        # print("按下了左箭头")
        game_state.piece.move_left()
    elif event.key == pygame.K_DOWN:
        reached_bottom = game_state.piece.move_down()
        if reached_bottom:
            game_state.piece = touch_bottom(game_area, game_state)
    elif event.key == pygame.K_UP:
        game_state.piece.turn_once()
    elif event.key == pygame.K_SPACE or event.key == pygame.K_d:
        game_state.piece.goto_bottom()
        touch_bottom(game_area, game_state)

    # print(game_area.score)
    # return piece


def touch_bottom(game_area, game_state):
    '''方块落到底部时，要消行，要生成新方块。如果触到顶部，游戏终止。'''
    game_state.add_score(game_area.eliminate_lines())
    for c in range(COLUMN_NUM):
        if game_area.is_wall(0, c):
            #game_area.draw_gameover()   #在这里绘制文字是不起作用的。必须放到主循环中。
            #print("game over!")
            game_state.gameover()
    game_state.new_piece()
    # print("game_state.piece:", game_state.piece)
    # return game_state.piece


def on_key_up(event, piece):
    if event.key == pygame.K_RIGHT:
        print("松开了右箭头")
    elif event.key == pygame.K_LEFT:
        print("松开了左箭头")

if __name__ == '__main__':
    main()
