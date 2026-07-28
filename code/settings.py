import pygame
from pathlib import Path

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

CODE_DIR = Path(__file__).parent.resolve()
ROOT_DIR = Path(CODE_DIR).parent.resolve()
DISPLAY_COLOR = pygame.Color("#2c497f")

TERMINAL_WH = (920, 620)
INPUT_WH = (920, 40)
GRID_WH = (300, 300)
