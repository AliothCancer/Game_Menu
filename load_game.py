# IMPORT
from pygame.sprite import Sprite
import pygame
from pygame.locals import *
# DEFINING CLASSES






# GLOBAL VARIABLES



# pygame initialization
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# game screen
GAME_TITLE = "GDRXY"
fps = 80
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(GAME_TITLE)
pygame.mouse.set_visible(True)

# CREATING CLASS OBJECT




# DEFINING FUNCTIONS

def event_handler():
    run = True
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    return run



def load_game():
    run = True
    while run:
        run = event_handler()
        pygame.display.flip()
        screen.fill((0, 100,0))

        clock.tick(fps)