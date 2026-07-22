import pygame
from settings import *
from pathlib import Path
from player_grid import Player_Grid, Map_Grid
from text_input import InputBox

class Game:
    def __init__(self):
        # SETUP-----------------------------------------------------------------
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("State of Emergency")

        self.clock = pygame.time.Clock()
        self.running = True
        self.player_char = pygame.font.Font(
            ROOT_DIR.joinpath("images", "Oxanium-Bold.ttf")
        )
        self.font = pygame.font.Font(
            ROOT_DIR.joinpath("images", "HackNerdFontMono-Regular.ttf"), 25
        )

        # GROUPS ---------------------------------------------------------------
        self.all_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()

        # SURFACES FOR GRIDWORK ------------------------------------------------
        self.grid_surface = pygame.Surface((300,300))
        self.grid_surface.set_colorkey("black")
            # default color for a surface is black
        self.player_surface = pygame.Surface((300,300))

        # TEXT ENTRY -----------------------------------------------
        self.text_entry = InputBox(self.font, self.all_sprites)

        # PLAYER AND MAP GRIDS -------------------------------------------------
        self.player_grid = Player_Grid(
            self.player_sprites,
            self.player_surface,
            self.player_char
        )

        self.map_grid = Map_Grid(
            self.grid_sprites,
            self.grid_surface,
            self.player_grid
        )

    def run(self):
        while self.running:

            dt = self.clock.tick(60) / 1000 # 0.017 seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # UPDATE -----------------------------------------------------------
            self.all_sprites.update(self.display_surface, dt)
            self.player_sprites.update(self.player_surface, dt)
            self.grid_sprites.update(self.grid_surface, self.player_grid, dt)

            # FILL (CLEAR), DRAW, BLIT -----------------------------------------
            self.display_surface.fill("#4b3885")
            self.player_surface.fill("black")

            self.player_sprites.draw(self.player_surface)
            self.all_sprites.draw(self.display_surface)

            self.saved_grid = self.grid_surface.copy()
            self.grid_surface.blit(self.saved_grid)
            self.grid_sprites.draw(self.saved_grid)

            self.display_surface.blit(self.player_surface, (20, 20))
            self.display_surface.blit(self.grid_surface, (20, 20))

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
