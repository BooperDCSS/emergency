import pygame
from pathlib import Path


class Player_Grid(pygame.sprite.Sprite):
    def __init__(self, groups, surface, font):
        super().__init__(groups)
        self.image = font.render("@", True, "#a1b2c3")
        self.rect = self.image.get_frect(
            center = ((surface.width / 2, surface.height / 2))
        )

    def draw_grid(self, surface):
        pygame.draw.rect(
            surface,
            "red",
            self.rect.inflate(15, 10).move(1, -1),
            3
        )

    def update(self, surface, dt):
        keys = pygame.key.get_just_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.centerx -= 25

        self.draw_grid(surface)


