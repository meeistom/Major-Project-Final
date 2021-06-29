# Filename: levels_instructions_screen.py
# Author: Tom Bednarek
# Date: June 2021

import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()


def levels_instructions_screen():
    PROGRAM_NAME = 'Digit Reboot'
    TITLE_FONT = 'Courier New'
    TEXT_FONT = 'Courier New'
    CONTINUE = 'Continue'
    BACK = 'Back'

    INSTRUCTIONS = 'Instructions'
    INSTRUCTIONS_1 = 'This program will teach you how to type.'
    INSTRUCTIONS_2 = 'The following screen will display a keyboard,'
    INSTRUCTIONS_3 = 'a text, as well as your left and right hands.'
    INSTRUCTIONS_4 = 'Follow how the hands type throughout the entire course'
    INSTRUCTIONS_5 = 'and you will be able to touch type.'
    INSTRUCTIONS_LST = [INSTRUCTIONS_1, INSTRUCTIONS_2, INSTRUCTIONS_3, INSTRUCTIONS_4, INSTRUCTIONS_5]

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TITLE_FONT_SIZE = 60
    TEXT_FONT_SIZE = 24
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    BACK_BOX_WIDTH = 200
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    CONTINUE_BOX_WIDTH = INPUT_BOX_WIDTH/2
    DESELECTED_THICKNESS = 1
    SELECTED_THICKNESS = 2

    LOGO = pygame.image.load("digit_reboot_logo.png")

    back_box_thickness = DESELECTED_THICKNESS
    continue_box_thickness = DESELECTED_THICKNESS

    ###### DISPLAY ######

    ### DISPLAY LOOP ###

    screen_width = 1366
    screen_height = round(screen_width*9/16)

    n=0
    colours = rainbow_colour()

    ### MAKE WINDOW AND SET CAPTION NAME ###

    screen = pygame.display.set_mode([screen_width, screen_height], RESIZABLE)
    pygame.display.set_caption(PROGRAM_NAME)
    pygame.display.set_icon(LOGO)

    ###

    running = True

    while running:

    ### SETUP SCREEN AND PUT TITLE ON SCREEN ###

        screen_width, screen_height = screen.get_size()
        screen.fill(WHITE)

        if n == 1530:
            n = 0

        title = Title(
            INSTRUCTIONS,
            TITLE_FONT,
            TITLE_FONT_SIZE,
            screen,
            colours[n],
            screen_width
        )

        title.blit()

    ###

    ### DRAW SCREEN BORDERS ###

        top_line = Rect(0, 0, screen_width, 2) # left, top, width, height
        right_line = Rect(screen_width-2, 0, 2, screen_height) # left, top, width, height
        bottom_line = Rect(0, screen_height-2, screen_width, 2) # left, top, width, height
        left_line = Rect(0, 0, 2, screen_height) # left, top, width, height
        lines=[top_line, right_line, bottom_line, left_line]

        border = Border(lines, screen, BLACK)
        border.draw_border()

        back_button = Button(
            BACK_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            BACK,
            back_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [screen_width-BACK_BOX_WIDTH-50, screen_height-INPUT_BOX_HEIGHT-50],
            [screen_width-BACK_BOX_WIDTH/2-50, (screen_height-INPUT_BOX_HEIGHT-50+TEXT_FONT_SIZE*1.5)]
        )

        continue_button = Button(
            CONTINUE_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            CONTINUE,
            continue_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-CONTINUE_BOX_WIDTH/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2)],
            [(screen_width/2), ((screen_height/2)+INPUT_BOX_HEIGHT*2.5)]
        )


        for i in range(len(INSTRUCTIONS_LST)):

            font = pygame.font.SysFont(TEXT_FONT, TEXT_FONT_SIZE)
            instruction_img = font.render(INSTRUCTIONS_LST[i], True, BLACK)
            instruction_rect = instruction_img.get_rect(center=[screen_width/2, screen_height/2-TEXT_FONT_SIZE*4+TEXT_FONT_SIZE*i*2]) # it always goes width then height

            screen.blit(instruction_img, instruction_rect)

        continue_button.init_box()
        continue_button.init_center_text()
        continue_button.blit_box(BLACK)
        continue_button.blit_center_text()

        back_button.init_box()
        back_button.init_center_text()
        back_button.blit_box(BLACK)
        back_button.blit_center_text()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                if continue_button.get_box().collidepoint(event.pos):
                    return 0
                
                elif back_button.get_box().collidepoint(event.pos):
                    return 1

            elif event.type == QUIT:
                return 2

        continue_box_thickness = SELECTED_THICKNESS if continue_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        back_box_thickness = SELECTED_THICKNESS if back_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS

        pygame.display.flip()
        n+=1


if __name__ == '__main__':
    levels_instructions_screen()
    pygame.quit()