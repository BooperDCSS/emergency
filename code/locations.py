class Location:
    def __init__(self, name, occupied=False, visited=False):
        self.name = name
        self.occupied = occupied
        self.visited = visited

        self.description_new = ""
        self.description_return = ""

        self.links = {} # direction/id pair
        self.interactions = {} # DETAIL/description pair
        self.items = {} # name/description pair
        self.scene_tracker = {} # tracks interactions within a scene to modify descriptions

location_01 = Location("the beginning", occupied=True, visited=True)
location_02 = Location("the trail")
location_03 = Location("the fields")

# LOCATION 1 -------------------------------------------------------------------
location_01.description_new = ("You awake in a well-lit room. As you rise to your feet, you notice an opening on one side, "
                               "like a CRACK in the WALL. A 'W' is engraved above it and a cool breeze issues from inside. "
                               "You cannot see WITHIN, but you hear the sound of wind issuing from it just as you notice the smell "
                               "of pine trees. Behind you is a similar opening with an 'E' above it. This OPENING is wider than "
                               "the other. You think you can see a SNOWMAN inside.\n")

location_01.description_return = "You return to the room where you first awoke. The blue light flashes as before, but you cannot ascertain when or how you were moved through the crevice."

location_01.links = {
    "w": location_02,
    "west": location_02,
    "e": location_03,
    "east": location_03
}

location_01.scene_tracker = {"paper": {"opening": "The light falls further into this opening. Unlike the exterior, the inside appears rough-hewn. As you get closer you notice a scrap of PAPER on the floor."},
                             "no paper": {"opening": "The light falls further into this opening. Unlike the exterior, the inside appears rough-hewn."},
                             }

location_01.interactions = {
    "crack": "It's seven or eight feet high and looks almost painted onto the wall. Standing close, you can see just a few feet inside. It is wide enough for you to walk through if you turn your body sideways.",
    "wall": "The walls feel like concrete, but are uniformly dark blue. Except for the cracks and letters on either side, they are practically featureless.",
    "within": "Just feet inside, the shadows condense to a flat, black void. Looking around, you realize no other SHADOWS are cast in the room, not even your own.",
    "shadows": "You don't have a shadow, and the room doesn't appear to have a light source. The featureless walls terminate in a featureless ceiling that must be 20 or more feet above.",
    "opening": location_01.scene_tracker["paper"]["opening"],
    "snowman": "Three faint, white circles, the largest of them on the bottom, are visible inside the 'E' opening. But no matter how close you get, the circles don't become any clearer."
}

location_01.items = {
    "paper": "It is a small scrap of plain white paper that reads 'follow the dot.'"
}

# LOCATION 2 -------------------------------------------------------------------
location_02.description_new = ("As you slip through the crack in the WALL, the light from the previous room suddenly dims, "
                               "then disappears. It is pitch black for a moment. Before you can move back, a blue "
                               "light flashes and you close your eyes. When they open, you find yourself on a PRECIPICE overlooking "
                               "a moonlit mountain pass. The LAND sinks into the distance, framed on either side by high cliffs, "
                               "sloping rock faces, THICKETS, and small clusters of trees. The moonlight seems to paint everything "
                               "beneath it in shades of GRAY.")

location_02.description_return = {"The night in this mountain pass is as still as it was the first time you saw it. Everything seems frozen in a gray sheet of light."}

location_02.links = {
    "e": location_01,
    "east": location_01
}

location_02.interactions = {
    "wall": "You turn to look at the crack in the wall, but find instead that there is a crack in the thin air just feet behind you. It disappears when you walk around it, as if it were perfectly flat. You can even walk through it from BEHIND.",
    "behind": "When you turn around, the rift is still there and you can see into its interior a few feet.",
    "precipice": "There is a maintained path that leads down into the valley below, but if you stepped forward, you would probably fall for the rest of your life."
}




