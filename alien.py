import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    #1 alien
    def __init__(self, ai_game):
        #create 1 alein
        super().__init__()
        self.screen=ai_game.screen

        #load image
        self.image = pygame.image.load("alien invasion/alien-invasion/images/alien.bmp")
        self.rect = self.image.get_rect()

        #new aliens
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #x position in float
        self.x = float(self.rect.x)