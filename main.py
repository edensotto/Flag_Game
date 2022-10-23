import random
import ScreenGrid
import Soldier
import consts
import pygame


def spread_grass():
    grass_width = random.randint(0, consts.WINDOW_WIDTH - grass1.get_width())
    grass_height = random.randint(0, consts.WINDOW_HEIGHT - grass1.get_height())
    return grass_width, grass_height


pygame.init()
pygame.display.set_caption('The Flag')
(width, height) = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
background = pygame.display.set_mode((width, height))
background.fill(consts.GREEN_COLOR)

for i in range(consts.GRASS_AMOUNT):
    grass = pygame.image.load(consts.GRASS_IMG)
    grass1 = pygame.transform.scale(grass, (consts.GRASS_WIDTH, consts.GRASS_HEIGHT))
    background.blit(grass1, spread_grass())


status = True

pygame.display.flip()
exit_game = False
game_over = False
ScreenGrid.create_screen_grid()
ScreenGrid.screen_grid[0][0] = consts.SOLDIER
print(ScreenGrid.screen_grid)
pos = Soldier.get_soldier_position()
pos_x = pos[0]
pos_y = pos[0]
coordinates = []

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():  # For Loop
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:

                background.fill(consts.BLACK_COLOR)
                for i in range(0, consts.WINDOW_WIDTH, consts.SQUARE_SIDE):
                    pygame.draw.line(background, consts.GREEN_COLOR, (i, 0), (i, 500), 1)
                for i in range(0, consts.WINDOW_HEIGHT, consts.SQUARE_SIDE):
                    pygame.draw.line(background, consts.GREEN_COLOR, (0, i), (1000, i), 1)
                pygame.display.flip()

            elif event.key == pygame.K_RIGHT:
                coordinates = Soldier.move_the_soldier(consts.RIGHT, pos_x, pos_y)
                x = coordinates[0]
                y = coordinates[1]

                background.blit(grass1, (x, y))
                pygame.display.flip()

                pos_x += consts.SQUARE_SIDE
                print(coordinates, pos_x, pos_y)

            elif event.key == pygame.K_LEFT:
                coordinates = Soldier.move_the_soldier(consts.LEFT, pos_x, pos_y)
                x = coordinates[0]
                y = coordinates[1]

                background.blit(grass1, (x, y))
                pygame.display.flip()

                pos_x -= consts.SQUARE_SIDE
                print(coordinates, pos_x, pos_y)


pygame.quit()
quit()


