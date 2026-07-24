import pygame
from settings import *

class Terminal_Output(pygame.sprite.Sprite):
    def __init__(self, font, groups, term_bg, display_surface, text="Where am I?\n"):
        super().__init__(groups)
        self.font = font
        self.text = text
        self.color = pygame.Color("#ffffff")
        self.updated = False
        self.scroll = False
        self.scroll_color = pygame.Color("#faee44")

        self.image = self.font.render(
            self.text,
            True,
            self.color,
            bgcolor="black",
            wraplength=900
        ).convert_alpha()

        self.rect = self.image.get_rect(topleft = (10, 10))
        self.bottom_y = self.rect.bottom

    def rewrite(self, groups, term_bg, display_surface):
        term_bg.fill("black")

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

        groups.draw(term_bg)
        display_surface.blit(term_bg, (340, 20))


    def render_again(self, groups, term_bg, display_surface):
        groups.draw(term_bg)
        display_surface.blit(term_bg, (340, 20))
        pygame.display.update()


    def scroll_terminal(self, groups, term_bg, display_surface):
        old_topleft = self.rect.topleft

        self.image = self.font.render(
            self.text,
            True,
            self.scroll_color,
            bgcolor="black",
            wraplength=900
        ).convert_alpha()

        self.render_again(groups, term_bg, display_surface)

        while self.scroll:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    term_bg.fill("black")
                    self.rect.top += 30
                    self.render_again(groups, term_bg, display_surface)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    term_bg.fill("black")
                    self.rect.top -= 30
                    self.render_again(groups, term_bg, display_surface)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    term_bg.fill("black")

                    self.image = self.font.render(
                        self.text,
                        True,
                        self.color,
                        bgcolor="black",
                        wraplength=900
                    ).convert_alpha()
                    self.rect = self.image.get_rect(topleft = old_topleft)
                    self.render_again(groups, term_bg, display_surface)

                    self.scroll = False

    def update(self, player_response, dt):
        if not player_response or player_response == "None":
            pass
        else:
            self.text += player_response
            self.updated = True


