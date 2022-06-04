import pygame
from pygame.sprite import Sprite

class Character(Sprite):

    def __init__(self,name,race):
        super().__init__()
        # initial info
        self.position = (0,0)
        self.name = name
        self.race = race
        self.level = 0

        # creating a info container
        self.info = {
            "Name": self.name,
            "Position": self.position,
            "Race": self.race,
            "Level": self.level
        }

    def get_info(self):
        return self.info


class Player(Character):
    def __init__(self,name,race):
        super(Player, self).__init__(name,race)
        self.vestiges = {
            "Superior clothes": None,
            "Inferior clothes": None,
            "Left hand": None,
            "Right Hand": None
        }
        self.inventary = { # example
        # "object_name": object_class
        }


class Monster(Character):
    pass


class Building:
    def __init__(self,name,position):
        self.name = name
        self.position = position
