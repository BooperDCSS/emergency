import pygame

class Inventory(pygame.sprite.Sprite):
    def __init__(self, font, groups, inv_surface, display_surface, main_character):
        super().__init__(groups)

        self.font = font
        self.groups = groups
        self.color = pygame.Color("#ffffff")

        self.inventory = main_character.inventory
        self.text = "\n".join(self.inventory)
        self.inv_surface = inv_surface
        self.display_surface = display_surface


        self.image = self.font.render(
            self.text,
            True,
            self.color,
            bgcolor="black",
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = (6, 10))
