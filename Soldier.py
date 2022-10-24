import ScreenGrid
import consts


def move_the_soldier(state, x, y):
    if state == consts.LEFT:
        return x-consts.SQUARE_SIDE, y
    elif state == consts.RIGHT:
        return x+consts.SQUARE_SIDE, y
    elif state == consts.UP:
        return x, y-consts.SQUARE_SIDE
    elif state == consts.DOWN:
        return x, y+consts.SQUARE_SIDE


def soldier_move(state, x, y):
    new_x, new_y = x, y
    if state == consts.LEFT:
        new_x -= 1
    if state == consts.RIGHT:
        new_x += 1
    if state == consts.UP:
        new_y -= 1
    if state == consts.DOWN:
        new_x += 1

    ScreenGrid.screen_grid[new_x][new_y] = ScreenGrid.screen_grid[x][y]
    ScreenGrid.screen_grid[x][y] = None


def get_soldier_position():
    screen_grid = ScreenGrid.screen_grid
    for i in range(len(screen_grid)):
        for j in range(len(screen_grid[i])):
            if screen_grid[i][j] == consts.SOLDIER:
                return i, j


def set_soldier_position(x, y):
    screen_grid = ScreenGrid.screen_grid
    screen_grid[x][y] = consts.SOLDIER

