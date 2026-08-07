import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT


def end_game(dt, font):
    concluding = True
    end_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    concluding_text_01 = "You step through the door and roll down the hill."
    sum_text = ""

    font_color = pygame.Color("#ffffff")

    while concluding:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                concluding = False

        for i in range(len(concluding_text_01)):
            end_surface.fill("black")
            image = font.render(
                sum_text + concluding_text_01[i],
                True,
                font_color,
                bgcolor="black",
                wraplength=1200,
            ).convert_alpha()
            sum_text += concluding_text_01[i]
            end_surface.blit(image, (40, 40))
            pygame.time.delay(60)
            pygame.display.update()


# narrative next
# hit 'ENTER' to continue
# two surfaces?
# render letter by letter as a final test
