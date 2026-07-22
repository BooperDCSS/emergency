import pygame
from settings import *

class Terminal_Output(pygame.sprite.Sprite):
    def __init__(self, font, groups, text="Where am I?\n"):
        super().__init__(groups)
        self.font = font
        self.text = text
        self.color = "#ffffff"

        self.image = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(344, 24, 910, 610)

    def update(self, new_text, dt):
        if not new_text or new_text == "None":
            return
        else:
            self.text += new_text
            if len(self.text) > 70:
                print("it's off the screen!")
            self.image = self.font.render(self.text, True, self.color)


