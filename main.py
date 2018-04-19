import sys
import random
import pygame
#各种配置
from settings import *
# from pieces import Piece
# from gamewall import GameWall
from gamestate import GameState
from game_display import GameDisplay
from game_resource import GameResource

def main():
    #初始化pygame
    pygame.init()
    # print(pygame.font.get_fonts())
    #创建屏幕对象
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    pygame.key.set_repeat(10, 100)  #一直按下某个键，每过100毫秒就引发一个KEYDOWN事件
    game_resource = GameResource()
    game_state = GameState(screen)

    game_resource.play_bg_music()

    #游戏主循环
    while True:
        #事件处理
        game_state = check_events(game_state, game_resource)

        #绘制游戏窗口
        GameDisplay.draw(screen, game_state, game_resource)

        #让最近绘制的屏幕可见
        pygame.display.flip()


def check_events(game_state, game_resource):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            game_state = on_key_down(event, game_state, game_resource)
        elif event.type == pygame.USEREVENT and not game_state.is_gameover:
            reached_bottom = game_state.piece.move_down()
            if reached_bottom:
                game_state.touch_bottom()
    return  game_state

def on_key_down(event, game_state, game_resource):
    if not game_state.is_paused and event.key == pygame.K_RIGHT:
        game_state.piece.move_right()
    elif not game_state.is_paused and event.key == pygame.K_LEFT:
        game_state.piece.move_left()
    elif not game_state.is_paused and event.key == pygame.K_DOWN:
        reached_bottom = game_state.piece.move_down()
        if reached_bottom:
            game_state.piece = game_state.touch_bottom()
    elif not game_state.is_paused and event.key == pygame.K_UP:
        game_state.piece.turn_once()
    elif not game_state.is_paused and (event.key == pygame.K_SPACE or event.key == pygame.K_d):
        game_state.piece.goto_bottom()
        game_state.touch_bottom()
    elif event.key == pygame.K_s and game_state.is_gameover:
        game_state.restart_game()
    elif event.key == pygame.K_p:
        if game_state.is_paused:
            game_state.resume_game()
        elif not game_state.is_gameover:
            game_state.pause_game()
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_r:
        game_state.restart_game()
    elif event.key == pygame.K_m:
        game_resource.pause_bg_music()

    return game_state


if __name__ == '__main__':
    main()
