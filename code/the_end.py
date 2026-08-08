import pygame
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, ROOT_DIR

# JUST FOR TESTING #############################################################
pygame.init()
main_font = pygame.font.Font(
    ROOT_DIR.joinpath("images", "HackNerdFontMono-Regular.ttf"), 25
)

inv_font = pygame.font.Font(
    ROOT_DIR.joinpath("images", "HackNerdFontMono-Regular.ttf"), 20
)
# JUST FOR TESTING #############################################################


def end_game(dt, font, small_font):
    concluding = True
    end_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    concluding_text_00 = (
        "The space on the other side of the door is dark. The moment you cross the threshold, "
        "your senses are battered with images and sounds that flash away in seconds. You try to absorb them, but it's as if "
        "your body were being shoved around at the same time. \n\nA small pond, a gigantic statue of Buddha, lights flashing "
        "from a monitor on Halloween night. You swing a bat and dive for second base in an instant..."
    )

    concluding_text_01 = (
        "\n\nClarity returns to you mid-tumble, as you roll down a short grassy rise. When you look "
        "up, you recognize everything. Piasa Island. The Mississippi. Sioux Power Station like a fortress on the bend. "
        "The sky is gray and you rub your arms in response to the cold. The river is filled with hunks of ice moving slowly "
        "downstream.\n\nYou notice the bodies floating in the river at the same time you notice the mirror near the shoreline."
    )

    concluding_text_02 = (
        "\n\nYou shudder at the sight of the mirror more than the bodies, but you walk the sandy path"
        " toward the mirror anyway."
    )

    concluding_text_03 = (
        "You get a sick feeling in your stomach that you know the people in the river. The feeling grows immeasurably "
        "worse when you finally reach the mirror and see yourself in it. You, or not you, is sitting in a reclining chair "
        "made of green fabric."
    )

    all_text = [concluding_text_00, concluding_text_01, concluding_text_02, concluding_text_03]
    current_index = 0
    animating = True
    sum_text = ""

    font_color = pygame.Color("#ffffff")

    pygame.event.clear()

    while concluding:

        if animating and current_index < len(all_text):
            for i in range(len(all_text[current_index])):
                end_surface.fill("black")
                image = font.render(
                    sum_text + all_text[current_index][i],
                    True,
                    font_color,
                    bgcolor="black",
                    wraplength=1200,
                ).convert_alpha()
                sum_text += all_text[current_index][i]
                end_surface.blit(image, (40, 40))
                pygame.time.delay(20)
                pygame.display.update()

            continue_image = small_font.render(
                "Press return to continue...", True, font_color, bgcolor="black"
            ).convert_alpha()
            end_surface.blit(continue_image, (1240 - continue_image.width, 680))
            pygame.display.update()

            animating = False

        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            concluding = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            current_index += 1

            if current_index == 3:
                sum_text = ""

            if current_index < len(all_text):
                animating = True
            else:
                concluding = False


end_game(0.017, main_font, inv_font)
