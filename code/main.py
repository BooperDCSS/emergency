import pygame
from settings import *
from pathlib import Path

class Game:
    def __init__(self):
        # SETUP-----------------------------------------------------------------
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("State of Emergency")

        self.clock = pygame.time.Clock()
        self.running = True

        # GROUPS ---------------------------------------------------------------
        self.all_sprites = pygame.sprite.Group()

    def run(self):
        while self.running:

            dt = self.clock.tick(60) / 1000 # 0.017 seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # UPDATE -----------------------------------------------------------
            # call update on sprite groups here

            # DRAW -------------------------------------------------------------
            self.display_surface.fill("purple")
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
