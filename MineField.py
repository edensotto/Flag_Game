import random
import ScreenGrid
import consts


# changes the default 'Empty' of the square to 'Bomb'
def change_matrix_state(row, col):
    ScreenGrid.screen_grid[row][col] = 'Mine'


# check if the soldier stepped on a mine
def is_on_mine(row, col):
    if ScreenGrid.screen_grid[row][col] == consts.MINE:
        return True
    else:
        return False


# check if the place in matrix is clear with no bombs
def is_clear(row, col):
    if col+2 >= consts.NUM_COLS or col-2 <= 0:
        return False

    elif is_on_mine(row, col+2) or is_on_mine(row, col-2):
        return False

    col -= 1
    if col < 0:
        return False

    else:
        for i in range(3):
            if is_on_mine(row, col):
                return False
            # if Object.is_touching_flag(row, col):
            #     print('False3 clear')
            #     return False
            col += 1

        return True


# pick a random place for a mine in the screen
def spread_a_mine():
    row_center = random.randint(0, consts.NUM_ROWS-1)
    col_center = random.randint(0, consts.NUM_COLS-1)

    while not is_clear(row_center, col_center):
        row_center = random.randint(0, consts.NUM_ROWS-1)
        col_center = random.randint(0, consts.NUM_COLS-1)

    return row_center, col_center


def calc_center_x(row):
    if row == 0:
        return 0
    else:
        return row*consts.SQUARE_SIDE


def calc_center_y(col):
    if col == 0:
        return 0
    else:
        return col*consts.SQUARE_SIDE


def calc_coordinate(coordinate):
    if coordinate == 0:
        return 0
    return coordinate//consts.SQUARE_SIDE

