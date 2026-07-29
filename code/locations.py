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
location_03 = Location("the apartments")

# LOCATION 1 -------------------------------------------------------------------
location_01.description_new = ("You awake in a well-lit room. As you rise to your feet, you notice an opening on one side, "
                               "like a CRACK in the WALL. A 'W' is engraved above it and a cool breeze issues from inside. "
                               "You cannot see WITHIN, but you hear the sound of running water just as you notice the smell "
                               "of pine trees. Behind you is a similar opening with an 'E' above it. This OPENING is wider than "
                               "the other. You think you can see a SNOWMAN inside.\n")

location_01.description_return = "You return to the room where you first awoke."

location_01.links = {
    "w": location_02,
    "west": location_02,
    "e": location_03,
    "east": location_03
}

location_01.interactions = {
    "crack": "It's seven or eight feet high and looks almost painted onto the wall. Standing close, you can see just a few feet inside. It is wide enough for you to walk through if you turn your body sideways.",
    "wall": "The walls feel like concrete, but are uniformly dark blue. Except for the cracks and letters on either side, they are practically featureless.",
    "within": "Just feet inside, the shadows condense to a flat, black void. Looking around, you realize no other SHADOWS are cast in the room, not even your own.",
    "shadows": "You don't have a shadow, and the room doesn't appear to have a light source. The featureless walls terminate in a featureless ceiling that must be 20 or more feet above.",
    "opening": "The light falls further into this opening. Unlike the exterior, the inside appears rough-hewn. As you get closer you notice a scrap of PAPER on floor.",

}

location_01.items = {
    "paper": "It is a small scrap of plain white paper that reads 'follow the dot.'"
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




