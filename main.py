import sys  

import pygame

from ship import Ship
from settings import Settings
from bullet import Bullet

class AlienInvasion:
    """ класс для управления ресурсами и поведением игры """
    def __init__(self):
        """инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen =pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        

        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #checks for input
            self._check_events()
            #creating everything on screen
            self._update_screen()
            #update ship position
            self.ship.update()
            #update bullets
            self.bullets.update()


    def _check_events(self):
        #event listener
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type==pygame.KEYUP:
                    self._check_keyup_events(event)
                    

    def _check_keydown_events(self, event):
        if event.key==pygame.K_RIGHT:
            #move to right
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            #move to left
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key==pygame.K_RIGHT:
            #stop move to right
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            #stop move to left
            self.ship.moving_left=False
        
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        #при каждом переходе меняет цвет на этот:
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Отображение последнего прорисованного экрана
        pygame.display.flip()


if __name__ =="__main__":
   #создание экзампяра и запуска игры
   ai = AlienInvasion()
   ai.run_game()