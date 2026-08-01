class Location:
    def __init__(self, name, occupied=False, visited=False):
        self.name = name
        self.occupied = occupied
        self.visited = visited

        self.description_new = ""
        self.description_observe = ""
        self.description_return = ""

        self.links = {} # direction/id pair for linked locations
        self.interactions = {} # DETAIL/description pair
        self.items = {} # name/description pair
        self.scene_tracker = {} # tracks interactions within a scene to modify descriptions

location_01 = Location("the beginning", occupied=True, visited=True)
location_02 = Location("the trail")
location_03 = Location("the fields")
location_04 = Location("the back yard")

# LOCATION 1 -------------------------------------------------------------------
location_01.description_new = ("You awake in a well-lit room. As you rise to your feet, you notice an opening on one side, "
                               "like a CRACK in the WALL. A 'W' is engraved above it and a cool breeze issues from inside. "
                               "You cannot see WITHIN, but you hear the sound of wind issuing from it just as you notice the smell "
                               "of pine trees. Behind you is a similar opening with an 'E' above it. This OPENING is wider than "
                               "the other. You think you can see a SNOWMAN inside.\n")

location_01.description_observe = ("You are in a well-lit room, but the source of light isn't obvious. There is an opening on one "
                                   "side, like a CRACK in the WALL. A 'W' is engraved above it and a cool breeze issues from inside. "
                                   "You cannot see WITHIN, but you hear the sound of wind issuing from it and you can smell pine in the air. "
                                   "Behind you is a similar opening with an 'E' above it. This OPENING is wider than the other. You think you "
                                   "can see something that looks like a SNOWMAN inside.")

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
    "snowman": "Three faint, white circles, the largest of them on the bottom, are visible inside the 'E' opening. But no matter how close you get, the circles don't become any clearer.",
    "w": "The letter 'W' is carved into the wall. The carving is smooth and polished.",
    "e": "The letter 'E' is marked out on the wall. Unlike the 'W', it appears to have been smashed out of the concrete with multiple blows of a hammer or chisel. It reminds you of a child's handwriting."
}

location_01.items = {
    "paper": "It is a small scrap of plain white paper that reads 'follow the dot.'"
}

# LOCATION 2 -------------------------------------------------------------------
location_02.description_new = ("As you slip through the crack in the WALL, the light from the previous room suddenly dims, "
                               "then disappears. It is pitch black for a moment. Before you can move back, a blue "
                               "light flashes and you close your eyes. When they open, you find yourself on a PRECIPICE overlooking "
                               "a moonlit mountain pass. The LAND sinks into the distance, framed on either side by high cliffs, "
                               "sloping rock faces, clumps of GRASS, and small clusters of trees. The moonlight seems to paint everything "
                               "beneath it in shades of GRAY.")

location_02.description_observe = ("You are on a PRECIPICE overlooking a moonlight mountain pass. The LAND sinks into the distance, framed "
                                   "on either side by high cliffs, sloping rock faces, clumps of GRASS, and small clusters of trees. The "
                                   "moonlight seems to paint everything beneath it in shades of GRAY.")

location_02.description_return = {"The night in this mountain pass is as still as it was the first time you saw it. Everything seems frozen in a gray sheet of light."}

location_02.links = {
    "e": location_01,
    "east": location_01
}

location_02.scene_tracker = {"cannister": {"grass": "Growing among the boulders and scrabble is a patch of high grass, against which a CANNISTER of some kind has been placed."},
                             "no cannister": {"grass": "Growing among the boulders and scrabble is a patch of high grass, many instances of which dot the valley before you."}}

location_02.interactions = {
    "wall": "You turn to look back at where you came from and find a rift, much like the crack you stepped through, hanging in thin air just feet behind you. It disappears when you walk around it, as if it were perfectly flat. You can even walk through it from BEHIND.",
    "behind": "When you turn around, the rift is still there and you can see into its interior a few feet.",
    "precipice": "There is a maintained path that leads into the valley below, but if you stepped forward, you would likely fall for the rest of your life.",
    "land": "The valley below looks like it was milled out of the earth by a gigantic tool, and the peaks around you stand like gravestones in this lunar light. You feel like a small mouse hiding in its enormity.",
    "grass": location_02.scene_tracker["cannister"]["grass"],
    "gray": "The light is peaceful and lonely at once. Everything is still, seemingly dead, and quiet. But then new sounds come into the silence and you hear the texture of the rocks and trees washing against the shore of the nighttime sky."
}

location_02.items = {
    "cannister": "It is a hard black cylinder the length of your forearm. On one end, the words 'Save the Bears' is raised on the surface. You also notice two silver circles with slits in them, above which an arrow and the word 'lock' is written. A button with the word 'push' below it is on the same side."
}


# LOCATION 3 -------------------------------------------------------------------

location_03.description_new = ("As you step into the darkness, the white circles get closer and closer, but remain a blur. "
                               "Just as you lean down to touch the top one, a blue light flashes. You raise your hands "
                               "and you shut your eyes for just a second. When they open, you are leaning over a melting "
                               "SNOWMAN with a carrot nose, stick arms, and coal eyes and buttons. It is wearing a red knit hat with a cardinal on it. "
                               "Stretching out around you in every direction are soybean FIELDS. The occasional tree rises high "
                               "above the HORIZON. You then realize you are standing on a two-lane HIGHWAY. You can see "
                               "another CRACK in the distance. Between it and you is a small pool of shiny LIQUID. Further "
                               "away, a ferris WHEEL stands frozen among a small group of low buildings.")

location_03.description_observe = ("You are standing above a SNOWMAN slowly melting on the HIGHWAY. It is wearing a red knit hat "
                                   "with a cardinal stitched on it. Stretching out around you in every direction are soybean "
                                   "FIELDS. The occasional tree rises high above the HORIZON. You can see another CRACK in the "
                                   "distance. Beyong it is a small pool of shiny LIQUID. Further away still, a ferris WHEEL "
                                   "stands frozen among a small group of low buildings."
                                   )

location_03.description_return = ("The soybean fields are hot, but the snowman remains half melted, its head tilted as if looking at the sun.")

location_03.links = {"w": location_01,
                     "west": location_01,
                     "s": location_04,
                     "south": location_04
                     }

location_03.scene_tracker = {"brick": {"liquid": "You become uneasy the closer you get to the liquid. It is red and spread out in a thick and uneven oval. On one end of the oval is a BRICK. It is clean, but you wonder at its presence. On the other end, a child's shoe sits, filled to the top with the red liquid."},
                             "no brick": {"liquid": "You are certain this is a pool of blood. The little shoe sitting in it makes you feel ill."}}

location_03.interactions = {"snowman": "The snowman is standing in a small puddle of water. There isn't a flake of snow anywhere else. The humidity hits you then, and you wipe sweap from the back of your neck.",
                            "fields": "Row upon row of soybean fan out into the distance at even intervals. Only a small, shallow ditch and the most vivid green grass you have ever seen stand between you and an endless supply of hairy green pods.",
                            "horizon": "The sky is the color of a bluejay, with huge puffy clouds and patches of darkness at the very edge of visibility. Lightning flashes in the hightest clouds, but you hear no thunder.",
                            "highway": "You check for cars in both directions, but see only the crack you must have emerged from and a long straight line of concrete dotted with yellow lines. The crack here appears to hover just above the pavement, and the letter 'W' is painted yellow below it.",
                            "crack": "A stark black tear is visible on the side of the road ahead, immediately to the right of a speed limit sign. You see another SIGN hanging below it.",
                            "sign": "A piece of fabric with the letter 'S' cut in the middle is hanging from a long thread wound around the lower bolt of the speed limit sign. The thread is sewn into the fabric in a recurring 'S' shape",
                            "liquid": location_03.scene_tracker["brick"]["liquid"],
                            "wheel": "When you first noticed it, the ferris wheel appeared stationary. Now, you wonder if it's moving every time you look away. "}
location_03.items = {"brick": "It is a jagged red brick with 10 holes in the middle of it. You don't understand why, but you want it in your hands... instead of someone else's."}


# LOCATION 4 -------------------------------------------------------------------
location_04.description_new = ("")
location_04.description_observe = ("")
location_04.description_return = ("")
location_04.links = {"n": location_03,
                     "north": location_03}
location_04.scene_tracker = {}
location_04.interactions = {}
location_04.items = {}




# location_XX.description_new = ("")
# location_XX.description_observe = ("")
# location_XX.description_return = ("")
# location_XX.links = {}
# location_XX.scene_tracker = {}
# location_XX.interactions = {}
# location_XX.items = {}
