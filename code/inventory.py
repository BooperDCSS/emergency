import pygame

class Inventory(pygame.sprite.Sprite):
    def __init__(self, font, groups, inv_surface, display_surface, main_character):
        super().__init__(groups)

        self.font = font
        self.groups = groups
        self.color = pygame.Color("#ffffff")
        self.main_character = main_character

        self.text = ""
        self.inv_surface = inv_surface
        self.display_surface = display_surface

        self.image = self.font.render(
            self.text,
            True,
            self.color,
            bgcolor="black",
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = (6, 10))

    def rewrite(self):
        self.text = "\n".join(self.main_character.inventory)
        self.image = self.font.render(
            self.text,
            True,
            self.color,
            bgcolor="black",
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = self.rect.topleft)
