import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect =  ai_game.screen.get_rect()
        
        #size of button
        self.height, self.width=50, 200
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #creating rect of object button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #once message appearance
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        #creates rectangle and centers a text
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect =  self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        #shows button
        self.screen.fill(self.button_color, self.rect )
        self.screen.blit(self.msg_image, self.msg_image_rect)