import pygame
from pathlib import Path


class Player_Grid(pygame.sprite.Sprite):
    def __init__(self, groups, surface, font):
        super().__init__(groups)
        self.image = font.render("@", True, "#a1b2c3")
        self.rect = self.image.get_frect(
            center = ((150, 150))
        )
        self.return_response = ""

    def move_player_icon(self, direction):
        match direction.lower():
            case "west" | "w":
                self.rect.centerx -= 30
                self.return_response += "You move west.\n"
            case "east" | "e":
                self.rect.centerx += 30
                self.return_response += "You move east.\n"
            case "north" | "n":
                self.rect.centery -= 35
                self.return_response += "You move north.\n"
            case "south" | "s":
                self.rect.centery += 35
                self.return_response += "You move south.\n"
            case _:
                self.return_response += f"Moving to the {direction} doesn't make sense in this game, friend.\n"


    def update(self, surface, action, dt):
        self.action = str(action)
        self.movement_check = self.action.lower().split()
        self.legal_move_verbs = ["go", "move", "walk", "travel"]
        self.directions = [
            "north", "south", "east", "west", "n", "s", "e", "w",
            "ne", "nw", "se", "sw"
        ]
        self.return_response = ""

        if not self.action or self.action == "None":
            pass
        elif self.movement_check[1] in self.legal_move_verbs:
            self.move_player_icon(self.movement_check[2])
        elif self.movement_check[1] in self.directions:
            self.move_player_icon(self.movement_check[1])
        else:
            pass




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


