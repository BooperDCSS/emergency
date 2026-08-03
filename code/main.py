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
            ROOT_DIR.joinpath("images", "HackNerdFontMono-Regular.ttf"), 20
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


    # FUNCTIONS FOR THE PARSER -------------------------------------------------


    def location_change(self, direction):

        location_name = self.main_character.location.name
        room_links = self.main_character.location.links
        links_alt = self.main_character.location.links_alt
        illegal_move = "There is no clear or safe path in that direction."

        if direction in room_links: # .keys() not required, that is default behavior
            self.player_grid.move_player_icon(direction)
            if location_name == "the fields" and self.main_character.dot:
                self.main_character.move_character(links_alt[direction])
            else:
                self.main_character.move_character(room_links[direction])

            self.grid_sprites.update()

            if not self.main_character.location.visited:
                location_desc = self.main_character.location.description_new
                self.main_character.location.visited = True
            else:
                location_desc = self.main_character.location.description_return

            self.terminal_output.location_change(self.player_grid.move_response, location_desc)
            self.player_grid.move_response = ""
        else:
            self.terminal_output.update_terminal_with(illegal_move)


    def get_item(self, words):
        room_items = self.main_character.location.items
        your_inventory = self.main_character.inventory

        for word in words:
            if word in room_items and not your_inventory:
                self.main_character.obtain(word)
                self.terminal_output.update_terminal_with(
                    f"You place the {word} in your backpack. Wait, did I wake up with this backpack?"
                )
                self.inventory.rewrite()
            elif word in room_items and len(your_inventory) > 0:
                self.main_character.obtain(word)
                self.terminal_output.update_terminal_with(
                    f"You store the {word} in your backpack."
                )
                self.inventory.rewrite()

    def resolve_interaction(self, item1, item2):
        pass
        # TODO: this will lookup how items can interact and return the
        # appropriate actions for the terminal, inventory, and player

        hidden_items = {
            "nursery rhyme": "Fuzzy Wuzzy was a bear... fuzzy wuzzy wasn't very fuzzy was he?"
        }

        environment_puzzles = {"nursery rhyme": "box"}

        container_dict = {
            "cannister": {"screwdriver": "nursery rhyme"},
            "screwdriver": {"cannister": "nursery rhyme"}
        }

        # if item1 in container_dict and item2 in container_dict[item1]...
        # then yield the value associated with item1 and add it to the
        # player's inventory

        # if item1 is in the environment_puzzles and item2 in the location
        # then print special text to terminal for further action, so maybe
        # the door opens and we can move north



    def use_item(self, action_words):
        room_interactions = self.main_character.location.interactions
        your_inventory = self.main_character.inventory

        illegal_move = "There is no clear or safe path in that direction."
        # TODO: be sure to place self.room_interactions with a new variable that
        # tracks room objects you can use items on; this is probably another
        # dictionary that tracks what happens when the inventory object is used
        # in that fashion, like your scene tracker

        use_prepositions = {"with", "on", "in"}
        common_articles = {"the", "a", "an"}

        # first possibility: a miskey, like "use the" or "use a"
        if len(action_words) == 2 and action_words[1] in common_articles:
            verb, _ = action_words
            self.terminal_output.update_terminal_with(
                f"Specify the thing you would like to {verb}."
            )

        # second possibility: "use key door," which will work, or a miskey
        # like "use key with" or "open box using"
        elif len(action_words) == 3 and action_words[1] in your_inventory:
            verb, item, word = action_words
            if word in your_inventory:
                print(f"You {verb} the {item} with the {word}.")
            elif word in room_interactions:
                print(f"You {verb} the {item} with the {word} in the room.")
            else:
                self.terminal_output.update_terminal_with(
                    f"Be more specific. How do you {verb} the {item}?"
            )

        # third variation: "use key with door"
        elif len(action_words) == 4 and action_words[1] in your_inventory:
            if action_words[2] in use_prepositions and action_words[3] in your_inventory:
                verb, item, prep, dir_object = action_words
                print(f"You {verb} the {item} {prep} the {dir_object}.")
            elif action_words[2] in use_prepositions and action_words[3] in room_interactions:
                verb, item, prep, dir_object = action_words
                print(f"You {verb} the {item} {prep} the {dir_object} in the room.")
            elif action_words[2] in use_prepositions:
                verb, item, prep, word = action_words
                print(f"You can't {verb} the {item} {prep} the {word}.")

        # fourth variation: "use the key door", which will work, or a miskey
        # like "use the key on"
        elif len(action_words) == 4 and action_words[1] in common_articles:
            if action_words[2] in your_inventory and action_words[3] in your_inventory:
                verb, article, item, dir_object = action_words
                print(f"You {verb} {article} {item} on the {dir_object}.")
            elif action_words[2] in your_inventory and action_words[3] in room_interactions:
                verb, article, item, dir_object = action_words
                print(f"You {verb} {article} {item} on the {dir_object} in the room.")
            else:
                verb, article, word1, word2 = action_words
                print(f"You want to {use} {article} {word1} with the... {word2}? You decide that makes no sense.")

        # fifth variation: something like "use the key on the door"
        elif len(action_words) > 4 and action_words[1] in common_articles:
            if action_words[2] in your_inventory:
                verb, article, item, *rest = action_words
                for word in rest:
                    if word in your_inventory:
                        print(f"You {verb} {article} {item} on the {word}.")
                    elif word in room_interactions:
                        print(f"You {verb} {article} {item} on the {word} in the room.")
            else:
                verb, article, *rest = action_words
                print(f"You want to {verb} {article} what...?! You think about it and change your mind.")

        # sixth variation: "use key with the door"
        elif len(action_words) > 4 and action_words[1] in your_inventory:
            pass


    def look_at(self, words):
        room_items = self.main_character.location.items
        room_interactions = self.main_character.location.interactions
        your_inventory = self.main_character.inventory

        for word in words:
            if word in room_interactions:
                self.terminal_output.update_terminal_with(
                    room_interactions[word]
                )
            elif word in room_items:
                self.terminal_output.update_terminal_with(
                    room_items[word]
                )
            elif word in your_inventory:
                self.terminal_output.update_terminal_with(
                    your_inventory[word]
                )


    # YE BIG OLDE PARSER -------------------------------------------------------
    # traffic control after the player inputs a command
    # relies on self.action_text; populated by self.input.handle_input(event)
    # TODO: look into event bus structures for possible future refactor

    def parse_action(self, dt):
        self.action_text = str(self.action_text).strip("> ").lower()
        action_words = self.action_text.split()

        if not action_words or action_words == ["none"]:
            return

        get_verbs = {"get", "grab"}
        look_verbs = {"inspect", "investigate", "look"}
        move_verbs = {"go", "move", "walk", "travel"}
        directions = {
            "north", "south", "east", "west", "northwest", "northeast",
            "southwest", "southeast", "n", "s", "e", "w", "nw", "ne", "sw", "se"
        }
        review_verbs = {"history", "review"}
        talk_verbs = {"talk"}
        use_verbs = {"use", "open"}
        no_comprende = "This game isn't sophisticated enough to understand what you want to do."
        the_scene = self.main_character.location.description_observe


        match action_words:
            case [verb, *words] if verb in get_verbs:
                self.get_item(words)
            case ["pick", "up", *words]:
                self.get_item(words)
            case [verb, *words] if verb in look_verbs:
                self.look_at(words)
            case ["look", "at", *words]:
                self.look_at(words)
            case [verb, direction] if verb in move_verbs and direction in directions:
                self.location_change(direction)
            case [direction] if direction in directions:
                self.location_change(direction)
            case [verb, *words] if verb in use_verbs:
                self.use_item(action_words)
            case ["history"] | ["review"]:
                self.terminal_output.scroll = True
                self.terminal_output.scroll_terminal(self.input, dt)
            case ["observe"]:
                self.terminal_output.update_terminal_with(the_scene)
            case _:
                self.terminal_output.update_terminal_with(no_comprende)


    # RUN: GAME LOOP USING EVERYTHING ABOVE ------------------------------------
    def run(self):

        # this background never changes; fill it once and then leave it alone
        self.display_surface.fill(DISPLAY_COLOR)

        # ensure initial conditions are correct for update and event text
        self.dirty = True
        self.action_text = ""

        # "rewrite" once to get the terminal on screen; update grid for first room
        self.terminal_output.rewrite()
        self.grid_sprites.update()
        pygame.display.flip()

        while self.running:

            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.action_text, changed = self.input.handle_input(event)

            self.parse_action(dt)

            if changed:
                self.dirty = True

            # RESET ACTION -----------------------------------------------------

            self.action_text = ""

            # FILL, DRAW, BLIT -------------------------------------------------
            self.input_surface.fill("black")
            self.input_sprites.draw(self.input_surface)
            self.display_surface.blit(self.input_surface, (340, 660))

            if self.dirty:
                self.player_surface.fill("black")
                self.inventory_surface.fill("black")

                self.player_sprites.draw(self.player_surface)
                self.inventory_sprites.draw(self.inventory_surface)

                self.saved_grid = self.grid_surface.copy()
                self.grid_surface.blit(self.saved_grid)
                self.grid_sprites.draw(self.saved_grid)

                self.display_surface.blit(self.player_surface, (20, 20))
                self.display_surface.blit(self.grid_surface, (20, 20))
                self.display_surface.blit(self.inventory_surface, (20, 340))

            if self.dirty and self.terminal_output.updated:
                self.terminal_surface.fill("black")
                self.terminal_output.rewrite()
                self.terminal_output.updated = False

            pygame.display.update()
            self.dirty = False

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
