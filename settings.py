class Settings():
    """Класс для хранения настроек"""
    
    def __init__(self):
        """"инициализирует настройки игры"""
        #параметры экрана
        self.screen_width = 840
        self.screen_height = 600
        self.bg_color = (0,0,0)
        #speed of ship
        self.ship_speed = 0.5
        #bullet characteristics
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 3