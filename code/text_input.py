import pygame
from settings import *

class InputBox(pygame.sprite.Sprite):
    def __init__(self, font, groups, text='What do you do?'):
        super().__init__(groups)
        self.inactive_color = "black"
        self.active_color = "blue"
        self.text = text

        self.image = font.render(text, True, self.inactive_color)
        self.rect = pygame.Rect(340, 660, 920, 40)

        self.active = False


