import pygame
from settings import *

class InputBox(pygame.sprite.Sprite):
    def __init__(self, font, groups, text='> Get, Look, Move'):
        super().__init__(groups)
        self.font = font
        self.inactive_color = pygame.Color("#00ffff")
        self.active_color = pygame.Color("#ffffff")
        self.color = self.inactive_color
        self.text = text

        self.image = self.font.render(text, True, self.color).convert_alpha()
        self.rect = pygame.Rect(344, 664, 920, 40)

        self.active = False


    def make_active(self):
        self.active = True
        self.text = "> "
        self.color = self.active_color
        self.changed = True

    def handle_event(self, event):
        self.action_response = None
        self.changed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.make_active()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            self.make_active()

        elif event.type == pygame.TEXTINPUT and self.active:
            self.text += event.text
            self.changed = True

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.action_response = self.text
                self.text = '> Get, Look, Move'
                self.active = False
                self.color = self.inactive_color
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            self.changed = True

        if self.changed:
            self.image = self.font.render(self.text, True, self.color).convert_alpha()

        return self.action_response, self.changed


