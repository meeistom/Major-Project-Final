# Filename: level_end_screen.py
# Author: Tom Bednarek
# Date: May 2021

import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()

def level_WPM_end_screen(level_or_wpm, account, wpm, accuracy):

    ###### CONSTANTS ######

    PROGRAM_NAME = 'Digit Reboot'
    TITLE_FONT = 'Courier New'
    TEXT_FONT = 'Courier New'
    WPM_TEST = 'WPM Test'
    FILL_CHAR = '0'
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TITLE_FONT_SIZE = 60
    TEXT_FONT_SIZE = 24
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    NEXT_AGAIN_BUTTON_WIDTH = MAIN_MENU_BUTTON_WIDTH = (INPUT_BOX_WIDTH - INPUT_BOX_HEIGHT)/2
    SELECTED_THICKNESS = 2
    DESELECTED_THICKNESS = 1
    LOGO = pygame.image.load("digit_reboot_logo.png")

    NEXT_AGAIN_TEXT = 'Next' if level_or_wpm == 0 else 'Again'
    MAIN_MENU_TEXT = 'Main Menu'

    ###### DISPLAY ######

    ### DISPLAY LOOP ###

    screen_width = 1366
    screen_height = 768
    next_again_box_thickness = DESELECTED_THICKNESS
    main_menu_box_thickness = DESELECTED_THICKNESS
    WPM_box_thickness = DESELECTED_THICKNESS
    accuracy_box_thickness = DESELECTED_THICKNESS
    n=0
    colours = rainbow_colour()

    ###

    #level = user.get_level()+1
    if level_or_wpm == 0:
        level = account.get_level()
        title_text = f'Level {fill_blanks(str(level), FILL_CHAR)}'
    else:
        title_text = WPM_TEST

    wpm_text = f'WPM: {wpm}'
    accuracy_text = f'Accuracy: {accuracy}%'

    ###

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
            title_text,
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

        WPM_box = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            wpm_text,
            WPM_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)-INPUT_BOX_HEIGHT*2)],
            [(screen_width/2), (screen_height/2)-INPUT_BOX_HEIGHT*1.5]
        )

        accuracy_box = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            accuracy_text,
            accuracy_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, (screen_height/2)],
            [(screen_width/2), (screen_height/2)+INPUT_BOX_HEIGHT/2]
        )

        next_again_button = Button(
            NEXT_AGAIN_BUTTON_WIDTH, 
            INPUT_BOX_HEIGHT,
            NEXT_AGAIN_TEXT,
            next_again_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)+INPUT_BOX_HEIGHT/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2)],
            [(screen_width/2)+(INPUT_BOX_HEIGHT+NEXT_AGAIN_BUTTON_WIDTH)/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2.5)]
        )

        main_menu_button = Button(
            MAIN_MENU_BUTTON_WIDTH, 
            INPUT_BOX_HEIGHT,
            MAIN_MENU_TEXT,
            main_menu_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-MAIN_MENU_BUTTON_WIDTH-INPUT_BOX_HEIGHT/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2)],
            [(screen_width/2)-(INPUT_BOX_HEIGHT+NEXT_AGAIN_BUTTON_WIDTH)/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2.5)]
        )

        WPM_box.init_box()
        WPM_box.init_center_text()
        WPM_box.blit_box(BLACK)
        WPM_box.blit_center_text()

        accuracy_box.init_box()
        accuracy_box.init_center_text()
        accuracy_box.blit_box(BLACK)
        accuracy_box.blit_center_text()

        next_again_button.init_box()
        next_again_button.init_center_text()
        next_again_button.blit_box(BLACK)
        next_again_button.blit_center_text()

        main_menu_button.init_box()
        main_menu_button.init_center_text()
        main_menu_button.blit_box(BLACK)
        main_menu_button.blit_center_text()

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                
                if next_again_button.get_box().collidepoint(event.pos):
                    return 0

                elif main_menu_button.get_box().collidepoint(event.pos):
                    return 1

            elif event.type == QUIT:
                return 2
            
        next_again_box_thickness = SELECTED_THICKNESS if next_again_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        main_menu_box_thickness = SELECTED_THICKNESS if main_menu_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS

        pygame.display.flip()
        n+=1



if __name__ == '__main__':
    level_WPM_end_screen(int(input('Level or WPM end: ')), Account('tom','bed'), 64, 89)
    pygame.quit()