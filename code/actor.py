class Main_Character:
    def __init__(self, location):
        self.location = location
        self.inventory = ["Bjork CD", "Coffee mug"]

    def move_character(self, new_location):
        self.location.occupied = False
        self.location = new_location
        new_location.occupied = True

