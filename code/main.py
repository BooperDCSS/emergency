import pygame
from settings import *
from locations import *
from pathlib import Path
from player_grid import Player_Grid, Map_Grid
from text_input import InputBox
from terminal_output import Terminal_Output
from actor import Main_Character
from inventory import Inventory
from special_interactions import unwrap_items, rearrange_room

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

        filter_words = {"the", "at"}

        for i in range(len(words) - 1):
            if words[i] in filter_words:
                words[i] = ""

        the_thing = " ".join(words).strip()

        self.main_character.obtain(the_thing)
        if the_thing in room_items and not your_inventory:
            self.terminal_output.update_terminal_with(
                f"You place the {the_thing} in your backpack. Wait, did I wake up with this backpack?"
            )
        elif the_thing in room_items and len(your_inventory) > 0:
            self.terminal_output.update_terminal_with(
                f"You store the {the_thing} in your backpack."
            )

        self.inventory.rewrite()

    def use_item(self, action_words):
        # TODO: be sure to replace self.room_interactions with a variable or
        # set of variables that manages interactable places of interest within
        # each room. You'll need to alter location.interactions, alter the links
        # and maybe do something else to make this work... should all be handlded
        # within this function...

        # may need a check_altered function too, for location.altered flag

        room_interactions = self.main_character.location.interactions
        your_inventory = self.main_character.inventory

        illegal_move = "There is no clear or safe path in that direction."

        common_prepositions = {"with", "on", "in", "at"}
        common_articles = {"the", "a", "an"}
        compound_items = {"yellow": "note"}

        for item in compound_items:
            for i in range(len(action_words) - 1):
                if action_words[i] in compound_items:
                    action_words.remove(compound_items[item])
                    action_words[i] = item + " " + compound_items[item]

        match action_words:

        # first possibility: a miskey, like "use the" or "use a"
            case [verb, article] if article in common_articles:
                self.terminal_output.update_terminal_with(
                    f"Specify the thing you would like to {verb}."
                    )


        # second possibility: "use key door," which will work, or a miskey
        # like "use key with" or "open box using"
            case [verb, item, word] if item in your_inventory:
                if word in your_inventory:
                    result = unwrap_items(item, word, self.main_character)
                    if result:
                        self.inventory.rewrite()
                        self.terminal_output.update_terminal_with(result)
                    else:
                        self.terminal_output.update_terminal_with(f"You try to use the {item} with the {word}, but nothing happens.")
                elif word in room_interactions:
                    result = rearrange_room(item, word)
                    if result:
                        self.terminal_output.update_terminal_with(result)
                    else:
                        self.terminal_output.update_terminal_with(f"You see no reason the {item} and the {word} would have anything to do with each other.")
                else:
                    self.terminal_output.update_terminal_with(
                        f"{verb.capitalize()} the {item} how? On what? You need to think through that some more."
                )

        # third variation: "use key with door"
            case [verb, item, word1, word2] if item in your_inventory:
                if word1 in common_prepositions and word2 in your_inventory:
                    print(f"You {verb} the {item} {word1} the {word2}.")
                elif word1 in common_prepositions and word2 in room_interactions:
                    print(f"You {verb} the {item} {word1} the {word2} in the room.")
                else:
                    print(f"You can't {verb} the {item} {word1} the {word2}.")

        # fourth variation: "use the key door", which will work, or a miskey
        # like "use the key on"
            case [verb, article, word1, word2] if article in common_articles:
                if word1 in your_inventory and word2 in your_inventory:
                    print(f"You {verb} {article} {word1} on the {word2}.")
                elif word1 in your_inventory and word2 in room_interactions:
                    print(f"You {verb} {article} {word1} on the {word2} in the room.")
                else:
                    print(f"You want to {verb} {article} {word1} with the... {word2}? You decide that makes no sense.")

        # fifth variation: something like "use the key on the door"
            case [verb, article, item, prep, *rest] if (article in common_articles and
            item in your_inventory and
            prep in common_prepositions
            ):
                for i in range(len(rest) - 1):
                    if rest[i] in common_prepositions or rest[i] in common_articles:
                        rest[i] = ""

                thing = " ".join(rest).strip()

                if thing in your_inventory:
                        print(f"You {verb} {article} {item} {prep} the {thing}.")
                elif thing in room_interactions:
                    print(f"You {verb} {article} {item} {prep} the {thing} in the room.")
                else:
                    print(f"You want to {verb} what...? You decide to clear your mind before you do something foolish.")

        # sixth variation: "use key with the door"
            case [verb, item, prep, article, *rest] if (item in your_inventory and
            prep in common_prepositions and
            article in common_articles
            ):

                for i in range(len(rest) - 1):
                    if rest[i] in common_prepositions or rest[i] in common_articles:
                        rest[i] = ""

                thing = " ".join(rest).strip()

                if thing in your_inventory:
                    print(f"You {verb} the {item} {prep} {article} {thing}.")
                elif thing in room_interactions:
                    print(f"you {verb} the {item} {prep} {article} {thing} in the room.")
                else:
                    print(f"You know you want to {verb} the {item}, but you need to think more carefully about how, and with what.")


    def look_at(self, words):
        room_items = self.main_character.location.items
        room_interactions = self.main_character.location.interactions
        your_inventory = self.main_character.inventory

        filter_words = {"the", "at"}

        for i in range(len(words) - 1):
            if words[i] in filter_words:
                words[i] = ""

        the_thing = " ".join(words).strip()

        if the_thing in room_interactions:
            self.terminal_output.update_terminal_with(
                room_interactions[the_thing]
            )
        elif the_thing in room_items:
            self.terminal_output.update_terminal_with(
                room_items[the_thing]
            )
        elif the_thing in your_inventory:
            self.terminal_output.update_terminal_with(
                your_inventory[the_thing]
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
