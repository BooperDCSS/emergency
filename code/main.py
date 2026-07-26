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
        self.input_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.terminal_sprites = pygame.sprite.Group()

        # SURFACES FOR GRIDWORK ------------------------------------------------
        self.grid_surface = pygame.Surface((300,300))
        self.grid_surface.set_colorkey("black")
            # default color for a surface is black
        self.player_surface = pygame.Surface((300,300))

        # IN-GAME TERMINAL------------------------------------------------------
        self.terminal_surface = pygame.Surface(
            (920, 620),
            pygame.SRCALPHA
        ).convert_alpha()

        self.terminal_output = Terminal_Output(
            self.font,
            self.terminal_sprites,
            self.terminal_surface,
            self.display_surface
        )

        # TEXT ENTRY -----------------------------------------------------------
        self.input_surface = pygame.Surface((920, 40), pygame.SRCALPHA).convert_alpha()
        self.input = InputBox(self.font, self.input_sprites, self.input_surface)

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


        # TURN BY TURN UPDATE VARIABLES ----------------------------------------
        # "dirty" meaning status has updated and we need to refresh
        self.dirty = True
        self.action_text = ""

    def update_grid_and_terminal(self):
        self.grid_sprites.update(self.grid_surface, self.player_grid)

        # the terminal update is going to need to take multiple potential actions
        # or I will need one function for updating movements and another for
        # handling events within each room

        self.terminal_sprites.update(self.player_grid.move_response)
        self.player_grid.move_response = ""
        self.dirty = True

    def parse_action(self):
        self.action_text = str(self.action_text).strip("> ").lower()
        action_words = self.action_text.split()

        get_verbs = ("get", "grab")
        look_verbs = ("inspect", "investigate", "look")
        move_verbs = ("go", "move", "walk", "travel")
        review_verbs = ("history", "review")
        talk_verbs = ("talk")
        directions = (
            "north", "south", "east", "west", "n", "s", "e", "w",
            "ne", "nw", "se", "sw"
        )

        if not action_words or action_words == ["none"]:
            return

        # my code is simple enough that this can probably be a match-case block
        if len(action_words) >= 2:
            if action_words[0] in get_verbs:
                print("get verbs detected")
            elif action_words[0] in look_verbs:
                print("look verbs detected")
            elif action_words[0] in move_verbs:
                self.player_grid.move_player_icon(action_words[1])
                self.update_grid_and_terminal()
        elif action_words[0] in directions:
            self.player_grid.move_player_icon(action_words[0])
            self.update_grid_and_terminal()
        elif action_words[0] in review_verbs:
            self.terminal_output.scroll = True
            self.terminal_output.scroll_terminal(self.input)

    def run(self):

        # this background never changes; fill it once and then leave it alone
        self.display_surface.fill("#4b3885")

        # TODO: instantiate the room and place a character inside the first one

        # "rewrite" once to get the terminal on screen; update grid for first room
        self.terminal_output.rewrite()
        self.grid_sprites.update(self.grid_surface, self.player_grid)

        pygame.display.flip()

        while self.running:

            dt = self.clock.tick(30) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.action_text, changed = self.input.handle_input(event)


            # this now performs most of my updates
            # contains code that matches actions and directs traffic
            self.parse_action()

            if changed:
                self.dirty = True

            # RESET ACTION -----------------------------------------------------

            self.action_text = ""

            # FILL, DRAW, BLIT -------------------------------------------------
            if self.dirty:
                self.player_surface.fill("black")

                self.input_sprites.draw(self.input_surface)
                self.player_sprites.draw(self.player_surface)

                self.saved_grid = self.grid_surface.copy()
                self.grid_surface.blit(self.saved_grid)
                self.grid_sprites.draw(self.saved_grid)

                self.display_surface.blit(self.input_surface, (340, 660))
                self.display_surface.blit(self.player_surface, (20, 20))
                self.display_surface.blit(self.grid_surface, (20, 20))

            if self.dirty and self.terminal_output.updated:
                self.terminal_output.rewrite()
                self.terminal_output.updated = False

            pygame.display.update()
            self.dirty = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
