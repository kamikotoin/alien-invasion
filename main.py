import sys 

import pygame

from ship import Ship
from settings import Settings

class AlienInvasion:
    """ класс для управления ресурсами и поведением игры """
    def __init__(self):
        """инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen =pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self.screen)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            #event listener
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            #при каждом переходе меняет цвет на этот:
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #Отображение последнего прорисованного экрана
            pygame.display.flip()

if __name__ =="__main__":
   #создание экзампяра и запуска игры
   ai = AlienInvasion()
   ai.run_game()