from locations import location_99, location_100


def unwrap_items(item1, item2, main_character):

    hidden_items = {
        "yellow note": "It's a small piece of yellow notecard paper. It reads 'Fuzzy Wuzzy was a bear... fuzzy wuzzy wasn't very fuzzy was he?'"
    }

    hidden_description = {
        "yellow note": "You unscrew the cannister and press the open button on the lid. The lid pops up and, with a little force, opens completely. Inside is a small YELLOW NOTE."
    }

    container_dict = {
        "cannister": {"screwdriver": "yellow note"},
        "screwdriver": {"cannister": "yellow note"},
    }

    if item1 in container_dict:
        sub_key = container_dict[item1]
        for k, v in sub_key.items():
            interactive_item = k
            contained_item = v
        if item2 == interactive_item:
            main_character.inventory[contained_item] = hidden_items[contained_item]
            return hidden_description[contained_item]
    else:
        return False


def rearrange_room(item, room_detail, main_character):

    modifiable_interactions = {
        location_99: {
            "door": "The door now stands open, the light from beyond it glowing clearly around the edges."
        },
        location_100: {
            "compartment": "The weight of papers and books that held the desk closed have been blown away by the exploding brick. Inside, you see a toy ROCKING HORSE.",
            "desk": "The desk appears undamaged by the explosion. In fact, you notice there's no debris anywhere in the room. It now sits open, its contents exposed for you to see.",
            "brain": "You hit the bullseye when you threw the brick at the brain. There is a large crack and a smudge of red dust on the board where the brick landed, but the brick itself has vanished."
            }
    }

    interaction_table = {
        "yellow note": {"box": location_99},
        "brick": {"brain": location_100}
    }

    modify_links = {
            "yellow note",
            "brick"
        }

    if item in interaction_table:
        table_sub_key = interaction_table[item]
        for k, v in table_sub_key.items():
            interactive_object = k
            location_of_change = v
        if room_detail == interactive_object:
            mod_sub_key = modifiable_interactions[location_of_change]
            for o, d in mod_sub_key.items():
                object_to_change = o
                new_description = d
                location_of_change.interactions[object_to_change] = new_description
            location_of_change.description_observe = location_of_change.description_observe_alt
        if item in modify_links:
            location_of_change.links = location_of_change.links_alt
        main_character.inventory.pop(item)
        return location_of_change.description_alt

    else:
        return False
