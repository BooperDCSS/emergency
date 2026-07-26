import pygame
from settings import *

class InputBox(pygame.sprite.Sprite):
    def __init__(self, font, groups, input_surface, text='> Get, Look, Move'):
        super().__init__(groups)
        self.font = font
        self.inactive_color = pygame.Color("#00ffff")
        self.active_color = pygame.Color("#ffffff")
        self.color = self.inactive_color

        self.text = text
        self.surface = input_surface
        self.surface_color = input_surface.fill("black")
        self.groups = groups

        self.image = self.font.render(self.text, True, self.color).convert_alpha()
        self.rect = self.image.get_rect(topleft = (4, 4))

        self.active = False

    def make_active(self):
        self.surface.fill("black")
        self.active = True
        self.text = "> "
        self.color = self.active_color
        self.changed = True

    def handle_input(self, event):
        self.action_text = None
        self.changed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.make_active()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            self.make_active()

        elif event.type == pygame.TEXTINPUT and self.active:
            self.surface.fill("black")
            self.text += event.text
            self.changed = True

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.surface.fill("black")
                self.action_text = self.text
                self.text = '> Get, Look, Move'
                self.active = False
                self.color = self.inactive_color
            elif event.key == pygame.K_BACKSPACE:
                self.surface.fill("black")
                self.text = self.text[:-1]
            self.changed = True

        if self.changed:
            self.image = self.font.render(self.text, True, self.color).convert_alpha()

        return self.action_text, self.changed
