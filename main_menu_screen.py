# Filename: login_screen.py
# Author: Tom Bednarek
# Date: May 2021

import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()

def main_menu_screen():

    ###### CONSTANTS ######

    PROGRAM_NAME = 'Digit Reboot'
    MAIN_MENU = 'Main Menu'
    TITLE_FONT = 'Courier New'
    TEXT_FONT = 'Courier New'
    LEVELS = 'Levels'
    WPM_TEST = 'WPM Test'
    STATISTICS = 'Statistics'
    LOG_OUT = 'Logout'
    SETTINGS = 'Settings'
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TITLE_FONT_SIZE = 60
    TEXT_FONT_SIZE = 24
    LOG_OUT_BOX_WIDTH = SETTINGS_BOX_WIDTH = 200
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    SELECTED_THICKNESS = 2
    DESELECTED_THICKNESS = 1
    LOGO = pygame.image.load("digit_reboot_logo.png")

    ###

    ###### DISPLAY ######

    ### DISPLAY LOOP ###

    screen_width = 1366
    screen_height = 768
    levels_box_thickness = DESELECTED_THICKNESS
    WPM_test_box_thickness = DESELECTED_THICKNESS
    statistics_box_thickness = DESELECTED_THICKNESS
    log_out_box_thickness = DESELECTED_THICKNESS
    settings_box_thickness = DESELECTED_THICKNESS
    n=0
    colours = rainbow_colour()

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
            MAIN_MENU,
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

        levels_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            LEVELS,
            levels_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)-INPUT_BOX_HEIGHT*2)],
            [(screen_width/2), ((screen_height/2)-INPUT_BOX_HEIGHT*1.5)]
        )

        WPM_test_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            WPM_TEST,
            WPM_test_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, (screen_height/2)],
            [(screen_width/2), ((screen_height/2)+INPUT_BOX_HEIGHT/2)]
        )

        statistics_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            STATISTICS,
            statistics_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2)],
            [(screen_width/2), ((screen_height/2)+INPUT_BOX_HEIGHT*2.5)]
        )

        log_out_button = Button(
            LOG_OUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            LOG_OUT,
            log_out_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [screen_width-LOG_OUT_BOX_WIDTH-50, screen_height-INPUT_BOX_HEIGHT-50],
            [screen_width-LOG_OUT_BOX_WIDTH/2-50, (screen_height-INPUT_BOX_HEIGHT-50+TEXT_FONT_SIZE*1.5)]
        )

        settings_button = Button(
            SETTINGS_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            SETTINGS,
            settings_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [50, screen_height-INPUT_BOX_HEIGHT-50],
            [SETTINGS_BOX_WIDTH/2+50, (screen_height-INPUT_BOX_HEIGHT-50+TEXT_FONT_SIZE*1.5)]
        )

        levels_button.init_box()
        levels_button.init_center_text()
        levels_button.blit_box(BLACK)
        levels_button.blit_center_text()

        WPM_test_button.init_box()
        WPM_test_button.init_center_text()
        WPM_test_button.blit_box(BLACK)
        WPM_test_button.blit_center_text()

        statistics_button.init_box()
        statistics_button.init_center_text()
        statistics_button.blit_box(BLACK)
        statistics_button.blit_center_text()

        log_out_button.init_box()
        log_out_button.init_center_text()
        log_out_button.blit_box(BLACK)
        log_out_button.blit_center_text()

        settings_button.init_box()
        settings_button.init_center_text()
        settings_button.blit_box(BLACK)
        settings_button.blit_center_text()

        for event in  pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                if levels_button.get_box().collidepoint(event.pos):
                    return 0

                elif WPM_test_button.get_box().collidepoint(event.pos):
                    return 1

                elif statistics_button.get_box().collidepoint(event.pos):
                    return 2

                elif log_out_button.get_box().collidepoint(event.pos):
                    return 3
            
                elif settings_button.get_box().collidepoint(event.pos):
                    return 4

            levels_box_thickness = SELECTED_THICKNESS if levels_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
            WPM_test_box_thickness = SELECTED_THICKNESS if WPM_test_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
            statistics_box_thickness = SELECTED_THICKNESS if statistics_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
            log_out_box_thickness = SELECTED_THICKNESS if log_out_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
            settings_box_thickness = SELECTED_THICKNESS if settings_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS

            if event.type == QUIT:
                return 5

        pygame.display.flip()
        n+=1



if __name__ == '__main__':
    main_menu_screen()
    pygame.quit()