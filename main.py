import random

import MineField
import ScreenGrid
import Soldier
import consts
import pygame

clock = pygame.time.Clock()
ScreenGrid.create_screen_grid()


def spread_grass():
    row = random.randint(0, consts.NUM_ROWS-1)
    col = random.randint(0, consts.NUM_COLS-1)

    # while ScreenGrid.is_on_grass(row, col):
    #     row = random.randint(0, consts.NUM_ROWS - 1)
    #     col = random.randint(0, consts.NUM_COLS - 1)

    coordinate_col = MineField.calc_center_y(row)
    coordinate_row = MineField.calc_center_x(col)

    return coordinate_row, coordinate_col


# def spread_grass():
#     grass_width = random.randint(0, consts.WINDOW_WIDTH - 50)
#     grass_height = random.randint(0, consts.WINDOW_HEIGHT - 50)
#     return grass_width, grass_height


def draw_soldier():
    for i in range(consts.NUM_ROWS):
        for j in range(consts.NUM_COLS):
            if ScreenGrid.screen_grid[i][j] == consts.SOLDIER:
                soldier = pygame.image.load(consts.SOLDIER_IMG)
                soldier1 = pygame.transform.scale(soldier, (consts.SOLDIER_WIDTH, consts.SOLDIER_HEIGHT))
                coordinate_x = MineField.calc_center_x(i)
                coordinate_y = MineField.calc_center_y(j)
                background.blit(soldier1, (coordinate_y, coordinate_x))


def draw_flag():
    flag = pygame.image.load(consts.FLAG_IMG)
    flag1 = pygame.transform.scale(flag, (consts.FLAG_WIDTH, consts.FLAG_HEIGHT))
    background.blit(flag1, (MineField.calc_center_x(46), MineField.calc_center_x(22)))


pygame.init()
pygame.display.set_caption('The Flag')
background = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

list_grass = []
tuple_grass_place = ()
for i in range(consts.GRASS_AMOUNT):
    tuple_grass_place = spread_grass()
    list_grass.append(tuple_grass_place)
print(list_grass)


def draw_mine():
    for i in range(consts.NUM_ROWS):
        for j in range(consts.NUM_COLS):
            if ScreenGrid.screen_grid[i][j] == consts.MINE:
                mine = pygame.image.load(consts.MINE_IMG)
                mine1 = pygame.transform.scale(mine, (consts.MINE_WIDTH, consts.MINE_HEIGHT))
                background.blit(mine1, (j * consts.SQUARE_SIDE, i * consts.SQUARE_SIDE))


def draw_grass():
    grass = pygame.image.load(consts.GRASS_IMG)
    grass1 = pygame.transform.scale(grass, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    for i in range(len(list_grass)):
        background.blit(grass1, list_grass[i])
        pygame.display.flip()


def draw_init_window():
    background.fill(consts.GREEN_COLOR)
    draw_grass()
    draw_soldier()
    draw_flag()
    pygame.display.flip()


def draw_dark_window():
    background.fill(consts.BLACK_COLOR)
    for i in range(0, consts.WINDOW_WIDTH, consts.SQUARE_SIDE):
        pygame.draw.line(background, consts.GREEN_COLOR, (i, 0), (i, consts.WINDOW_HEIGHT), 1)
    for j in range(0, consts.WINDOW_HEIGHT, consts.SQUARE_SIDE):
        pygame.draw.line(background, consts.GREEN_COLOR, (0, j), (consts.WINDOW_WIDTH, j), 1)
    draw_mine()
    pygame.display.flip()


status = True
exit_game = False
game_over = False
ScreenGrid.create_screen_grid()
ScreenGrid.screen_grid[3][1] = consts.RIGHT_LEG
Soldier.set_soldier_position(0, 0)
pos = Soldier.get_soldier_position()
pos_x = pos[0]
pos_y = pos[1]
coordinates = []

draw_init_window()
pygame.display.flip()


# Creating a game loop
while not exit_game:
    for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                draw_dark_window()
                draw_init_window()
                pygame.display.update()
                clock.tick(10)

            elif event.key == pygame.K_RIGHT:
                coordinates = Soldier.move_the_soldier(consts.RIGHT, pos_x, pos_y)
                x = coordinates[1]
                y = coordinates[0]

                index_row = MineField.calc_coordinate(pos_y)
                index_col = MineField.calc_coordinate(pos_x)

                ScreenGrid.screen_grid[index_row][index_col] = consts.EMPTY
                pos_x += consts.SQUARE_SIDE

                index_row = MineField.calc_coordinate(x)
                index_col = MineField.calc_coordinate(y)

                Soldier.set_soldier_position(index_row, index_col)

                draw_init_window()
                pygame.display.update()
                print(coordinates, pos_x, pos_y)

                for i in range(25):
                    print(ScreenGrid.screen_grid[i])

            elif event.key == pygame.K_LEFT:
                coordinates = Soldier.move_the_soldier(consts.LEFT, pos_x, pos_y)
                x = coordinates[1]
                y = coordinates[0]

                index_col = MineField.calc_coordinate(pos_x)
                index_row = MineField.calc_coordinate(pos_y)

                ScreenGrid.screen_grid[index_row][index_col] = consts.EMPTY
                pos_x -= consts.SQUARE_SIDE

                index_row = MineField.calc_coordinate(x)
                index_col = MineField.calc_coordinate(y)

                Soldier.set_soldier_position(index_row, index_col)

                draw_init_window()
                pygame.display.update()
                print(coordinates, pos_x, pos_y)

            elif event.key == pygame.K_UP:
                coordinates = Soldier.move_the_soldier(consts.UP, pos_x, pos_y)
                x = coordinates[1]
                y = coordinates[0]

                index_col = MineField.calc_coordinate(pos_x)
                index_row = MineField.calc_coordinate(pos_y)

                ScreenGrid.screen_grid[index_row][index_col] = consts.EMPTY
                pos_y -= consts.SQUARE_SIDE

                index_row = MineField.calc_coordinate(x)
                index_col = MineField.calc_coordinate(y)

                Soldier.set_soldier_position(index_row, index_col)

                draw_init_window()
                pygame.display.update()
                print(coordinates, pos_x, pos_y)

            elif event.key == pygame.K_DOWN:
                coordinates = Soldier.move_the_soldier(consts.DOWN, pos_x, pos_y)
                x = coordinates[1]
                y = coordinates[0]

                index_col = MineField.calc_coordinate(pos_x)
                index_row = MineField.calc_coordinate(pos_y)

                ScreenGrid.screen_grid[index_row][index_col] = consts.EMPTY
                pos_y += consts.SQUARE_SIDE

                index_row = MineField.calc_coordinate(x)
                index_col = MineField.calc_coordinate(y)

                Soldier.set_soldier_position(index_row, index_col)

                draw_init_window()
                pygame.display.update()
                print(coordinates, pos_x, pos_y)


pygame.quit()
quit()


