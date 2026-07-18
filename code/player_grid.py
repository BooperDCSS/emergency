import pygame
from pathlib import Path


class Player_Grid(pygame.sprite.Sprite):
    def __init__(self, groups, surface, font):
        super().__init__(groups)
        self.image = font.render("P", True, "#a1b2c3")
        self.rect = self.image.get_frect(
            center = ((surface.width / 2, surface.height / 2))
        )
        self.padded_rect = self.rect.inflate(5, 5)
