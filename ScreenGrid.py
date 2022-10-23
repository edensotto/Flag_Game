import consts

screen_grid = []


def create_screen_grid():
    for rows in range(consts.NUM_ROWS):
        current_line = []
        for cols in range(consts.NUM_COLS):
            current_line.append(consts.EMPTY)
        screen_grid.append(current_line)
