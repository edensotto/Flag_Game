import pygame

import consts

pygame.init()
(width, height) = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
