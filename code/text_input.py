import pygame
from settings import *

class InputBox(pygame.sprite.Sprite):
    def __init__(self, font, groups, text='> What do you do?'):
        super().__init__(groups)
        self.font = font
        self.inactive_color = "#00ffff"
        self.active_color = "#ffffff"
        self.color = self.inactive_color
        self.text = text

        self.image = self.font.render(text, True, self.color)
        self.rect = pygame.Rect(344, 664, 920, 40)

        self.active = False


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.text = "> "
                self.color = self.active_color
            else:
                self.active = False

        if event.type == pygame.TEXTINPUT:
            self.text += event.text

        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    action_response = self.text
                    self.text = '> What do you do now?'
                    self.active = False
                    self.color = self.inactive_color
                    return action_response
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]

        self.image = self.font.render(self.text, True, self.color)


