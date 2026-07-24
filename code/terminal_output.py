import pygame
from settings import *

class Terminal_Output(pygame.sprite.Sprite):
    def __init__(self, font, groups, text="Where am I?\n"):
        super().__init__(groups)
        self.font = font
        self.text = [text]
        self.text_count = 0
        self.history = []
        self.color = pygame.Color("#ffffff")

        self.image = self.font.render(
            self.text[0],
            True,
            self.color,
            bgcolor="black",
            wraplength=900
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = (10, 10))
        self.text_height = self.image.get_height()

    def update(self, player_response, dt):
        if not player_response or player_response == "None":
            pass
        else:
            self.text.append(player_response)
            self.text_count += 1

            self.image = self.font.render(
                self.text[self.text_count],
                True,
                self.color,
                bgcolor="black",
                wraplength=900
            ).convert_alpha()

            self.text_height = self.image.get_height()
            self.rect = self.image.get_rect(topleft = (10, self.text_height + (self.text_count * 30)))


