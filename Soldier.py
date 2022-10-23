import ScreenGrid
import consts


def move_the_soldier(state, x, y):
    if state == consts.LEFT:
        return x, y-consts.SQUARE_SIDE
    elif state == consts.RIGHT:
        return x, y+consts.SQUARE_SIDE
    elif state == consts.UP:
        return x-consts.SQUARE_SIDE, y
    elif state == consts.DOWN:
        return x+consts.SQUARE_SIDE, y


def get_soldier_position():
    screen_grid = ScreenGrid.screen_grid
    for i in range(len(screen_grid)):
        for j in range(len(screen_grid[i])):
            if screen_grid[i][j] == consts.SOLDIER:
                return i, j


def set_soldier_position(x, y):
    pos = get_soldier_position()
    pos_x = pos[0]
    pos_y = pos[1]

    screen_grid = ScreenGrid.screen_grid
    screen_grid[pos_x][pos_y] = consts.EMPTY
    screen_grid[x][y] = consts.SOLDIER

