import pygame
from pathlib import Path

class Location:
    def __init__(self, id, name, description, occupied=False, visited=False):
        self.id = id
        self.name = name
        self.description = description
        self.occupied = occupied
        self.visited = visited

        self.links = {} # direction/id pair?
        self.interactions = {} # detail of interest / description pair
        self.items = {} # name/description pair?

description_01 = "You are in a well-lit room. You notice your shadow is missing."
location_01 = Location(1, "the beginning", description_01, occupied=True, visited=True)
