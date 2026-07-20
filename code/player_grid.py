import pygame
from pathlib import Path


class Player_Grid(pygame.sprite.Sprite):
    def __init__(self, groups, surface, font):
        super().__init__(groups)
        self.image = font.render("@", True, "#a1b2c3")
        self.rect = self.image.get_frect(
            center = ((150, 150))
        )

    def update(self, surface, dt):
        keys = pygame.key.get_just_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.centerx -= 35


class Map_Grid(pygame.sprite.Sprite):
    def __init__ (self, groups, surface, player):
        super().__init__(groups)
        self.image = pygame.Surface((25,30))
        self.rect = self.image.get_frect(center = (player.rect.center))

    def update(self, surface, player, dt):
        self.rect = self.image.get_frect(center = (player.rect.center))
        pygame.draw.rect(
            surface,
            "red",
            self.rect,
            3
        )


