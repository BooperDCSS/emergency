import pygame
from pathlib import Path

class Location:
    def __init__(self, id, description, occupied=False, visited=False):
        self.id = id
        self.description = description
        self.occupied = occupied
        self.visited = visited

        self.links = {} # direction/id pair?
        self.interactions = {} # detail of interest / description pair
        self.items = {} # name/description pair?
