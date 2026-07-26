import pygame
from pathlib import Path


class Player_Grid(pygame.sprite.Sprite):
    def __init__(self, groups, font):
        super().__init__(groups)
        self.image = font.render("@", True, "#a1b2c3")
        self.rect = self.image.get_frect(
            center = ((150, 150))
        )
        self.move_response = ""

    def move_player_icon(self, direction):
        match direction:
            case "west" | "w":
                self.rect.centerx -= 30
                self.move_response += "You move west.\n"
            case "east" | "e":
                self.rect.centerx += 30
                self.move_response += "You move east.\n"
            case "north" | "n":
                self.rect.centery -= 35
                self.move_response += "You move north.\n"
            case "south" | "s":
                self.rect.centery += 35
                self.move_response += "You move south.\n"
            case _:
                self.move_response += f"Moving to the {direction} doesn't make sense in this game, friend.\n"

class Map_Grid(pygame.sprite.Sprite):
    def __init__ (self, groups, surface, player):
        super().__init__(groups)
        self.image = pygame.Surface((25,30))
        self.rect = self.image.get_frect(center = (player.rect.center))

    def update(self, surface, player):
        self.rect = self.image.get_frect(center = (player.rect.center)).move(1,-1)
        pygame.draw.rect(
            surface,
            "red",
            self.rect,
            3
        )


