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

TEMPLATE_WIDTH = 5
TEMPLATE_HEIGHT = 5
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

I_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.O..',
                     '.O..'],
                    ['....',
                     'OOOO',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['OO',
                     'OO']]

J_SHAPE_TEMPLATE = [['O...',
                     'OOO.',
                     '....'],
                    ['.OO.',
                     '.O..',
                     '.O..'],
                    ['OOO.',
                     '..O.',
                     '....'],
                    ['..O.',
                     '..O.',
                     '.OO.']]

L_SHAPE_TEMPLATE = [['..O.',
                     'OOO.',
                     '....'],
                    ['.O..',
                     '.O..',
                     '.OO.'],
                    ['....',
                     'OOO.',
                     'O...'],
                    ['.OO.',
                     '..O.',
                     '..O.']]

T_SHAPE_TEMPLATE = [['.O..',
                     'OOO.',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '.O..'],
                    ['....',
                     'OOO.',
                     '.O..'],
                    ['..O.',
                     '.OO.',
                     '..O.']]

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}
