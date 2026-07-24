import pygame
from settings import *
from pathlib import Path
from player_grid import Player_Grid, Map_Grid
from text_input import InputBox
from terminal_output import Terminal_Output

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

        pygame.key.start_text_input()

        # GROUPS ---------------------------------------------------------------
        self.all_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.terminal_sprites = pygame.sprite.Group()

        # SURFACES FOR GRIDWORK ------------------------------------------------
        self.grid_surface = pygame.Surface((300,300))
        self.grid_surface.set_colorkey("black")
            # default color for a surface is black
        self.player_surface = pygame.Surface((300,300))

        # TEXT ENTRY -----------------------------------------------------------
        self.input = InputBox(self.font, self.all_sprites)
        self.input_background = pygame.Surface((920, 40))

        # IN-GAME TERMINAL------------------------------------------------------
        self.terminal_output = Terminal_Output(self.font, self.terminal_sprites)
        self.terminal_background = pygame.Surface((920, 620), pygame.SRCALPHA).convert_alpha()
        self.terminal_background.fill("black")

        # PLAYER AND MAP GRIDS -------------------------------------------------
        self.player_grid = Player_Grid(
            self.player_sprites,
            self.player_char
        )

        self.map_grid = Map_Grid(
            self.grid_sprites,
            self.grid_surface,
            self.player_grid
        )


        # TURN BY TURN UPDATE VARIABLE -----------------------------------------
        # "dirty" meaning status has updated and we need to refresh
        self.dirty = True

    def run(self):
        while self.running:

            dt = self.clock.tick(30) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                action_response, changed = self.input.handle_event(event)
                if changed:
                    self.dirty = True


            # UPDATE -----------------------------------------------------------
            self.all_sprites.update(self.display_surface, dt)
            self.player_sprites.update(self.player_surface, action_response, dt)
            self.grid_sprites.update(self.grid_surface, self.player_grid, dt)

            if self.player_grid.return_response:
                self.terminal_sprites.update(self.player_grid.return_response, dt)
                self.player_grid.return_response = ""
                self.dirty = True

            action_response = ""

            # FILL (CLEAR), DRAW, BLIT -----------------------------------------
            if self.dirty:
                self.display_surface.fill("#4b3885")
                self.player_surface.fill("black")


                self.display_surface.blit(self.input_background, (340, 660))
                self.player_sprites.draw(self.player_surface)
                self.all_sprites.draw(self.display_surface)
                self.terminal_sprites.draw(self.terminal_background)

                self.saved_grid = self.grid_surface.copy()
                self.grid_surface.blit(self.saved_grid)
                self.grid_sprites.draw(self.saved_grid)

                self.display_surface.blit(self.player_surface, (20, 20))
                self.display_surface.blit(self.grid_surface, (20, 20))

                self.display_surface.blit(self.terminal_background, (340, 20))


                pygame.display.update()
                self.dirty = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
