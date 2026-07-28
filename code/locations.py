class Location:
    def __init__(self, name, occupied=False, visited=False):
        self.name = name
        self.occupied = occupied
        self.visited = visited

        self.description_new = ""
        self.description_return = ""

        self.links = {} # direction/id pair
        self.interactions = {} # DETAIL / description pair
        self.items = {} # name/description pair

location_01 = Location("the beginning", occupied=True, visited=True)
location_02 = Location("the trail")

# LOCATION 1 -------------------------------------------------------------------
location_01.description_new = ("You awake in a well-lit room. As you rise to "
                               "your feet, you notice an opening on one side, "
                               "like a CRACK in the WALL. A 'W' is engraved "
                               "above it and a cool breeze issues from inside. "
                               "You cannot see WITHIN, but you hear the sound "
                               "of running water just as you smell pine in the air."
                               " Behind you is a similar opening with an 'E' above it."
                               " This opening is wider than the other. You "
                               "think you can see a SNOWMAN inside.\n")

location_01.description_return = "You return to the room where you first awoke."

location_01.links = {
    "w": location_02,
    "west": location_02,
    "e": "placeholder2"
}

location_01.interactions = {
    "crack": "It's seven, maybe eight feet high, and just wide enough for you to walk through if you turn your body sideways.",
    "wall": "They look and feel like concrete and are painted dark blue. Aside from the cracks, they are perfect uniform."
}

# LOCATION 2 -------------------------------------------------------------------
location_02.description_new = ("As you slip through the crack in the wall, all the light from the previous room dims, "
                               "then blinks out. It is pitch black for a moment. Before you can move backward, a blue "
                               "light flashes and stings your eyes. You find yourself beside a STREAM.")

location_02.links = {
    "e": location_01,
    "east": location_01
}

location_02.interactions = {
    "stream": "It looks cold."
}




