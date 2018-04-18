SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900
CELL_WIDTH = 40
COLUMN_NUM = 10
LINE_NUM = 20
GAME_AREA_WIDTH = CELL_WIDTH * COLUMN_NUM
GAME_AREA_HEIGHT = CELL_WIDTH * LINE_NUM
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT
EDEG_COLOR = (0, 0, 0)
CELL_COLOR = (100, 100, 100)
BG_COLOR = (230, 230, 230)

HANZI_COLOR = (0, 0, 0)
SCORE_LABEL_COLOR = (0, 0, 0)
GAMEOVER_COLOR = (255, 0, 0)
TITLE_COLOR = (0, 0, 255)


# TEMPLATE_WIDTH = 5
# TEMPLATE_HEIGHT = 5



SHAPES = 'SZIOJLT'
S_SHAPE_TEMPLATE = [['.OO.',
                     'OO..',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '..O.']]

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..']]

I_SHAPE_TEMPLATE = [['OOOO',
                     '....',
                     '....',
                     '....'],
                    ['.O..',
                     '.O..',
                     '.O..',
                     '.O..']
                    ]

O_SHAPE_TEMPLATE = [['OO',
                     'OO']]

J_SHAPE_TEMPLATE = [['..O.',
                     '..O.',
                     '.OO.'],
                    ['O...',
                     'OOO.',
                     '....'],
                    ['.OO.',
                     '.O..',
                     '.O..'],
                    ['OOO.',
                     '..O.',
                     '....']
                    ]

L_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.OO.'],

                    ['....',
                     'OOO.',
                     'O...'],

                    ['.OO.',
                     '..O.',
                     '..O.'],

                    ['..O.',
                     'OOO.',
                     '....'],
                    ]

T_SHAPE_TEMPLATE = [
                    ['OOO.',
                     '.O..',
                     '....'],

                    ['..O.',
                     '.OO.',
                     '..O.'],

                    ['.O..',
                     'OOO.',
                     '....'],

                    ['.O..',
                     '.OO.',
                     '.O..'],
                    ]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

PIECE_COLORS = {
    'S': (0, 255, 128),
    'Z': (255, 128, 255),
    'J': (128, 0, 255),
    'L': (0, 0, 255),
    'I': (255, 255, 0),
    'O': (255, 0, 0),
    'T': (255, 128, 0)
}

BLANK_LABEL = '-'    #20*10游戏区域中，单元格表示为'-'，意味着为空。
TIMER_INTERVAL = 1000   #最开始方块每个1000ms下降1行。