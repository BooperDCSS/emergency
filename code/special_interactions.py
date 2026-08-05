from main import main_character

def unwrap_items(self, item1, item2):

    hidden_items = {
        "yellow note": "It's a small piece of yellow notecard paper. It reads 'Fuzzy Wuzzy was a bear... fuzzy wuzzy wasn't very fuzzy was he?'"
    }

    container_dict = {
        "cannister": {"screwdriver": "yellow note"},
        "screwdriver": {"cannister": "yellow note"}
    }

    if item1 in container_dict:
        sub_key = container_dict[item1]
        for k, v in sub_key.items():
            interactive_item = k
            contained_item = v
        if item2 == interactive_item:
            main_character.inventory[contained_item] = hidden_items[contained_item]
            return True
    else:
        return False
