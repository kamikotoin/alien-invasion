import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #control bullet

    def __init__(self, ai_game):
        #object of bullet
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #creating a bullet at 0 0 position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #bullet current position
        self.y = float(self.rect.y)


    def update(self):
        #updates position of bullet
        self.y-=self.settings.bullet_speed
        self.rect.y=self.y

    def draw_bullet(self):
        #draws a bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)