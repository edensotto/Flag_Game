import random
import ScreenGrid
import Object
import consts


# changes the default 'Empty' of the square to 'Bomb'
def change_matrix_state(row, col):
    ScreenGrid.screen_grid[row][col] = 'Mine'


# check if the place in matrix is clear with no bombs
def is_clear(row, col):
    col -= 1
    if col < 0:
        return False

    else:
        for i in range(consts.MINE_WIDTH):
            if not ScreenGrid.screen_grid[row][col] == 'EMPTY' or Object.is_touching_flag(row, col):
                return False
            col += 1
        return True


# pick a random place for a mine in the screen
def spread_a_mine():
    current_row_center = random.randint(0, consts.NUM_ROWS)
    current_col_center = random.randint(0, consts.NUM_COLS)

    while not is_clear(current_row_center, current_col_center):
        current_row_center = random.randint(0, consts.NUM_ROWS)
        current_col_center = random.randint(0, consts.NUM_COLS)

    return current_row_center, current_col_center


# check if the soldier stepped on a mine
def is_on_mine(row, col):
    if ScreenGrid.screen_grid[row][col] != 'Empty':
        return True
    else:
        return False


def calc_center_x(col):
    return col*consts.SQUARE_SIDE - consts.SQUARE_SIDE


def calc_center_y(row):
    return row*consts.SQUARE_SIDE - consts.SQUARE_SIDE
