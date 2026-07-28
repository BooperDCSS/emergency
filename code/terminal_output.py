import pygame
from settings import *

class Terminal_Output(pygame.sprite.Sprite):
    def __init__(self, font, groups, term_bg, display_surface, text):
        super().__init__(groups)
        self.font = font
        self.text = text
        self.color = pygame.Color("#ffffff")
        self.scroll_color = pygame.Color("#faee44")

        self.groups = groups
        self.term_bg = term_bg
        self.display_surface = display_surface

        self.updated = False
        self.scroll = False

        self.image = self.font.render(
            self.text,
            True,
            self.color,
            bgcolor="black",
            wraplength=900
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = (10, 10))
        self.bottom_y = self.rect.bottom

    def rewrite(self):
        self.term_bg.fill("black")

        self.image = self.font.render(
            self.text,
            True,
            self.color,
            bgcolor="black",
            wraplength=900
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = self.rect.topleft)
        self.bottom_y = self.rect.bottom

        if self.bottom_y >= 600:
            self.rect.top -= 330
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
            self.bottom_y = self.rect.bottom

        self.groups.draw(self.term_bg)
        self.display_surface.blit(self.term_bg, (340, 20))


    def render_again(self):
        self.groups.draw(self.term_bg)
        self.display_surface.blit(self.term_bg, (340, 20))
        pygame.display.update()


    def scroll_terminal(self, input):
        old_topleft = self.rect.topleft

        input.text = "Up/Down arrow to scroll. ESC to return."
        input.image = input.font.render(
            input.text,
            True,
            self.scroll_color
        ).convert_alpha()

        input.surface.fill("black")
        input.groups.draw(input.surface)
        self.display_surface.blit(input.surface, (340, 660))

        self.image = self.font.render(
            self.text,
            True,
            self.scroll_color,
            bgcolor="black",
            wraplength=900
        ).convert_alpha()

        self.render_again()

        while self.scroll:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.term_bg.fill("black")
                    self.rect.top += 30
                    self.render_again()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.term_bg.fill("black")
                    self.rect.top -= 30
                    self.render_again()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.term_bg.fill("black")

                    input.text = '> Get, Look, Move'
                    input.image = input.font.render(
                        input.text,
                        True,
                        self.color
                    ).convert_alpha()

                    input.surface.fill("black")
                    input.groups.draw(input.surface)
                    self.display_surface.blit(input.surface, (340, 660))

                    self.image = self.font.render(
                        self.text,
                        True,
                        self.color,
                        bgcolor="black",
                        wraplength=900
                    ).convert_alpha()
                    self.rect = self.image.get_rect(topleft = old_topleft)
                    self.render_again()

                    self.scroll = False

    def update(self, move_response):
        if not move_response or move_response == "None":
            pass
        else:
            self.text += move_response
            self.updated = True


