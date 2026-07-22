import pygame
from pathlib import Path


class Player_Grid(pygame.sprite.Sprite):
    def __init__(self, groups, surface, font):
        super().__init__(groups)
        self.image = font.render("@", True, "#a1b2c3")
        self.rect = self.image.get_frect(
            center = ((150, 150))
        )

    def update(self, surface, action, dt):
        action = str(action)
        if "west" in action:
            self.rect.centerx -= 30
        elif "east" in action:
            self.rect.centerx += 30
        elif "north" in action:
            self.rect.centery -= 35
        elif "south" in action:
            self.rect.centery += 35


class Map_Grid(pygame.sprite.Sprite):
    def __init__ (self, groups, surface, player):
        super().__init__(groups)
        self.image = pygame.Surface((25,30))
        self.rect = self.image.get_frect(center = (player.rect.center))

    def update(self, surface, player, dt):
        self.rect = self.image.get_frect(center = (player.rect.center)).move(1,-1)
        pygame.draw.rect(
            surface,
            "red",
            self.rect,
            3
        )


