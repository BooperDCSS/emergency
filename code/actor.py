from locations import *

class Main_Character:
    def __init__(self, location):
        self.location = location
        self.inventory = {}
        self.dot = False

    def move_character(self, new_location):
        self.location.occupied = False
        self.location = new_location
        new_location.occupied = True

    def obtain(self, item):
        self.inventory[item] = self.location.items[item]

        # this routine logic ensures that the environment updates when the
        # character picks up items. It uses a scene tracking dictionary in the
        # locations class to sub in new descriptions for that environment detail
        if item in self.location.scene_tracker:
            sub_key = self.location.scene_tracker[f"no {item}"]
            for k, v in sub_key.items():
                interaction_key = k
                new_interaction_value = v
                self.location.interactions[interaction_key] = new_interaction_value

        if item == "dot":
            self.dot = True
        self.location.items.pop(item)





