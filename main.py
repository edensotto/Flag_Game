import pygame
import consts

pygame.init()
(width, height) = (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()


# set the pygame window name
pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
image = pygame.image.load("path").convert()

# Using blit to copy content from one surface to other
screen.blit(image, (0, 0))

# paint screen one time
pygame.display.flip()
status = True

while (status):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library
pygame.quit()
