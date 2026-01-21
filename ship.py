import pygame

class Ship():
    """Класс для управления кораблем"""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицую"""
        self.screen = ai_game.screen
        self.screen_rect =ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        #Загружает изображения корабля и получает прямоугольник
        self.image=pygame.image.load("alien invasion/alien-invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        #Каждый новый корабль повляется у нижнего экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #cordinate of ship 
        self.x=float(self.rect.x)

        #is moving or not
        self.moving_right=False
        self.moving_left=False
        


    def update(self):\
        #updates coordinates x
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x-=self.settings.ship_speed
        #updates ingame coordinates
        self.rect.x=self.x
        
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x=float(self.rect.x)

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
    
