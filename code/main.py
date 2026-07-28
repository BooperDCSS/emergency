import pygame
from settings import *
from locations import *
from pathlib import Path
from player_grid import Player_Grid, Map_Grid
from text_input import InputBox
from terminal_output import Terminal_Output
from actor import Main_Character
from inventory import Inventory

class Game:
    def __init__(self):
        # SETUP-----------------------------------------------------------------
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Who am I?")

        self.clock = pygame.time.Clock()
        self.running = True

        self.player_char = pygame.font.Font(
            ROOT_DIR.joinpath("images", "Oxanium-Bold.ttf")
        )

        self.font = pygame.font.Font(
            ROOT_DIR.joinpath("images", "HackNerdFontMono-Regular.ttf"), 25
        )

        self.inv_font = pygame.font.Font(
            ROOT_DIR.joinpath("images", "Oxanium-Bold.ttf"), 20
        )

        pygame.key.start_text_input()


        # THE ACTOR!! ----------------------------------------------------------
        self.main_character = Main_Character(location_01)


        # GROUPS ---------------------------------------------------------------
        self.input_sprites = pygame.sprite.Group()
        self.grid_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.terminal_sprites = pygame.sprite.Group()
        self.inventory_sprites = pygame.sprite.Group()


        # SURFACES FOR GRIDWORK ------------------------------------------------
        self.grid_surface = pygame.Surface(GRID_WH)
        self.grid_surface.set_colorkey("black")
            # default color for a surface is black
        self.player_surface = pygame.Surface(GRID_WH)


        # IN-GAME TERMINAL------------------------------------------------------
        self.terminal_surface = pygame.Surface(
            TERMINAL_WH,
            pygame.SRCALPHA
        ).convert_alpha()

        self.terminal_output = Terminal_Output(
            self.font,
            self.terminal_sprites,
            self.terminal_surface,
            self.display_surface,
            self.main_character.location.description_new
        )


        # TEXT ENTRY -----------------------------------------------------------
        self.input_surface = pygame.Surface(INPUT_WH, pygame.SRCALPHA).convert_alpha()
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

        # INVENTORY SURFACE AND DATA -------------------------------------------
        self.inventory_surface = pygame.Surface(INV_WH, pygame.SRCALPHA).convert_alpha()
        self.inventory = Inventory(
            self.inv_font,
            self.inventory_sprites,
            self.inventory_surface,
            self.display_surface,
            self.main_character
        )


    # ADDITIONAL GAME FUNCTIONS
    # TERMINAL OUTPUT (TOP) FUNCTIONS ------------------------------------------


    def top_location_change(self):
        self.grid_sprites.update(self.grid_surface, self.player_grid)

        if not self.main_character.location.visited:
            location_desc = self.main_character.location.description_new
            self.main_character.location.visited = True
        else:
            location_desc = self.main_character.location.description_return

        self.terminal_output.top_location_change(self.player_grid.move_response, location_desc)
        self.player_grid.move_response = ""
        self.dirty = True


    # YE BIG OLDE PARSER -------------------------------------------------------
    # this is the main traffic control after the player inputs a command
    # it relies on self.action_text, which is populated by self.input.handle_input(event)

    def parse_action(self):
        self.action_text = str(self.action_text).strip("> ").lower()
        action_words = self.action_text.split()

        room_links = self.main_character.location.links

        illegal_move_text = "There is no clear or safe path in that direction."

        get_verbs = {"get", "grab"}
        look_verbs = {"inspect", "investigate", "look"}
        move_verbs = {"go", "move", "walk", "travel"}
        review_verbs = {"history", "review"}
        talk_verbs = {"talk"}
        directions = {
            "north", "south", "east", "west", "n", "s", "e", "w",
            "ne", "nw", "se", "sw"
        }

        if not action_words or action_words == ["none"]:
            return

        match action_words:
            case [verb, *rest] if verb in get_verbs:
                print("Get verbs detected")
            case ["pick", "up", *rest]:
                print("You used the 'pick up' variation")
            case [verb, *rest] if verb in look_verbs:
                print("Look verbs detected")
            case ["look", "at", *rest]:
                print("You used the 'look at' variation")
            case [verb, direction] if verb in move_verbs and direction in directions:
                if direction in room_links: # .keys() not required, that is default behavior
                    self.player_grid.move_player_icon(direction)
                    self.main_character.move_character(room_links[direction])
                    self.top_location_change()
                else:
                    self.terminal_output.top_illegal_move(illegal_move_text)
                    self.dirty = True
            case [direction] if direction in directions:
                if direction in room_links:
                    self.player_grid.move_player_icon(direction)
                    self.main_character.move_character(room_links[direction])
                    self.top_location_change()
                else:
                    self.terminal_output.top_illegal_move(illegal_move_text)
                    self.dirty = True
            case ["history"] | ["review"]:
                self.terminal_output.scroll = True
                self.terminal_output.scroll_terminal(self.input)


    def run(self):

        # this background never changes; fill it once and then leave it alone
        self.display_surface.fill(DISPLAY_COLOR)

        # ensure initial conditions are correct for update and event text
        self.dirty = True
        self.action_text = ""

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
                self.inventory_surface.fill("black")

                self.input_sprites.draw(self.input_surface)
                self.player_sprites.draw(self.player_surface)
                self.inventory_sprites.draw(self.inventory_surface)

                self.saved_grid = self.grid_surface.copy()
                self.grid_surface.blit(self.saved_grid)
                self.grid_sprites.draw(self.saved_grid)

                self.display_surface.blit(self.input_surface, (340, 660))
                self.display_surface.blit(self.player_surface, (20, 20))
                self.display_surface.blit(self.grid_surface, (20, 20))
                self.display_surface.blit(self.inventory_surface, (20, 340))

            if self.dirty and self.terminal_output.updated:
                self.terminal_output.rewrite()
                self.terminal_output.updated = False

            pygame.display.update()
            self.dirty = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
