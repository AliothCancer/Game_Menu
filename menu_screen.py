from pygame.sprite import Sprite
from pygame.locals import *
import pygame
from time import sleep


class Text(Sprite):

    def __init__(self, text, font_dimension,
                    x_pos, y_pos, color="White", font=None):

        super().__init__()

        global counter, textes

        self.sound = pygame.mixer.Sound("sound_effect/menu/menu_sound_effect.mp3")
        self.font = font
        self.color = color
        self.textes = {id:self}
        self.active_color = False
        self.reactive_mouse = True
        self.selected_text = "_> " + text + "    "
        self.normal_text = text
        self.font_dimension = font_dimension
        self.x_pos, self.y_pos = x_pos, y_pos

        # init font
        self.text_font = pygame.font.Font(self.font, self.font_dimension)

        # sprite class need self.image and self.rect
        self.image = self.text_font.render(self.normal_text, True, self.color)

        # get the rect of image
        self.rect = self.image.get_rect()
        self.rect.center = [self.x_pos, self.y_pos]



    def update(self):
        x,y = pygame.mouse.get_pos()

        #self.rect.collidepoint(x,y)
        if self.reactive_mouse and self.rect.collidepoint(x,y):
            color = (200,0,200)
            self.image = self.text_font.render(self.selected_text, True, color)
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_pos, self.y_pos]

        #self.rect.collidepoint(x,y)
        elif not self.rect.collidepoint(x,y) :
            self.image = self.text_font.render(self.normal_text, True, self.color)
            self.rect = self.image.get_rect()
            self.rect.center = [self.x_pos, self.y_pos]






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

pygame.mixer.music.load("sound_effect/menu/menu_sound_effect.mp3")


def event_handler(sprite_obj):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        for spr in sprite_obj.sprites():
            x, y = pygame.mouse.get_pos()
            if spr.rect.collidepoint(x, y):
                # pygame.mixer.music.play()

                if (event.type == pygame.MOUSEBUTTONDOWN):

                    choosen_option = spr.normal_text
                    print(choosen_option)
                    return choosen_option


def process_key_pressed(list_lenght,sprite_selector,
                        sprite_option_midleft,selector_counter):
    #clock.tick(15)
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_a]:
        pass

    elif pressed[pygame.K_d]:
        pass

    elif pressed[pygame.K_s] and selector_counter+1 != list_lenght:
        selector_counter += 1
        sprite_selector.x_pos, sprite_selector.y_pos = sprite_option_midleft[selector_counter]
        sprite_selector.x_pos -= 63

    elif pressed[pygame.K_w] and selector_counter!=0:
        selector_counter -= 1
        sprite_selector.x_pos, sprite_selector.y_pos = sprite_option_midleft[selector_counter]
        sprite_selector.x_pos -= 63

    print(selector_counter,list_lenght)
    if selector_counter == list_lenght :
        selector_counter = 0
        sprite_selector.x_pos, sprite_selector.y_pos = sprite_option_midleft[selector_counter]
        sprite_selector.x_pos -= 63

    return selector_counter


def menu_screen(selector_counter):

    font_dimension = 50
    menu_options = [
            "Start a new game",
            "Load a game",
            "Settings",
            "Exit"
        ]


    menu = pygame.sprite.Group()

    # mouse sprite
    #mouse = Mouse(screen)
    #menu.add(mouse)



    # title sprite
    #                            font    xpos ypos
    title = Text(GAME_TITLE,font_dimension*2,800,450 - 200,
                 color="Red", font="font/Game_Of_Squids.ttf")
    title.reactive_mouse = False
    menu.add(title)

    # options sprite
    y_space = 100
    for n,text in enumerate(menu_options):
        x = screen_width//2
        y = screen_height//2 + n * y_space
        sprite_text = Text(text, font_dimension, x,y,
                           font="font/Game_Of_Squids.ttf")
        menu.add(sprite_text)

    del x,y
    sprite_options_midleft = [spr.rect.midleft for spr in menu.sprites()[1:]]

    # selector sprite
    x,y= menu.sprites()[1].rect.midleft
    sprite_selector = Text("_>",font_dimension,
                           x,y,color=(255,0,255),font="font/Game_Of_Squids.ttf")
    sprite_selector.reactive_mouse = False
    sprite_selector.x_pos -= 63
    menu.add(sprite_selector)



    choosen_option = None




    while True:
        if choosen_option != None:
            break
        selector_counter = process_key_pressed(len(sprite_options_midleft),sprite_selector,
                            sprite_options_midleft,selector_counter)
        sleep(0.08)
        choosen_option = event_handler(menu)
        pygame.display.flip()
        screen.fill((0,0,50))

        menu.draw(screen)
        menu.update()
        clock.tick(fps)

    return choosen_option