import pygame
from settings import *
from pathlib import Path
from player_grid import Player_Grid

class Game:
    def __init__(self):
        # SETUP-----------------------------------------------------------------
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("State of Emergency")

        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(ROOT_DIR.joinpath("images", "Oxanium-Bold.ttf"))

        # GROUPS ---------------------------------------------------------------
        self.all_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()

        # SURFACES -------------------------------------------------------------
        self.grid_surface = pygame.Surface((300,300))

        # PLAYER GRID ----------------------------------------------------------
        self.player_grid = Player_Grid(
            self.grid_sprites,
            self.grid_surface,
            self.font
        )

    def run(self):
        while self.running:

            dt = self.clock.tick(60) / 1000 # 0.017 seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # UPDATE -----------------------------------------------------------
            self.grid_sprites.update(self.grid_surface, dt)

            # DRAW -------------------------------------------------------------
            self.display_surface.fill("purple")
            self.display_surface.blit(self.grid_surface, (20,20))
            self.saved_grid = self.grid_surface.copy()
            self.grid_surface.blit(self.saved_grid)

            self.all_sprites.draw(self.display_surface)
            self.grid_sprites.draw(self.grid_surface)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
