# Filename: statistics_screen.py
# Author: Tom Bednarek
# Date: May 2021

import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()

def statistics_screen(account):

    ###### CONSTANTS ######

    PROGRAM_NAME = 'Digit Reboot'
    STATISTICS = 'Statistics'
    TITLE_FONT = 'Courier New'
    TEXT_FONT = 'Courier New'
    BACK = 'Back'
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TITLE_FONT_SIZE = 60
    TEXT_FONT_SIZE = 24
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    BACK_BOX_WIDTH = 200
    SELECTED_THICKNESS = 2
    DESELECTED_THICKNESS = 1
    LOGO = pygame.image.load("digit_reboot_logo.png")

    ###

    account_level = f'Level: {account.get_level()}'
    average_wpm = f'Average WPM: {account.get_average_WPM()}'
    highest_wpm = f'Highest WPM: {account.get_highest_WPM()}'
    last_10_average_wpm = f'Last 10 Average WPM: {account.get_last_10_average_WPM()}'
    total_keypresses = f'Total Keypresses: {account.get_total_keypresses()}'
    join_date = f'Join Date: {account.get_join_date()}'
    # total_key_presses
    # MAYBE last_10_average_wpm


    ###### DISPLAY ######

    ### DISPLAY LOOP ###

    screen_width = 1366
    screen_height = round(screen_width*9/16)
    level_box_thickness = DESELECTED_THICKNESS
    average_wpm_box_thickness = DESELECTED_THICKNESS
    highest_wpm_box_thickness = DESELECTED_THICKNESS
    total_keypresses_box_thickness = DESELECTED_THICKNESS
    last_10_average_wpm_box_thickness = DESELECTED_THICKNESS
    join_date_box_thickness = DESELECTED_THICKNESS
    back_box_thickness = DESELECTED_THICKNESS
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
            STATISTICS,
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

    ###


        level_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT*6,
            account_level,
            level_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)-INPUT_BOX_HEIGHT*2.5)],
            [(screen_width/2), ((screen_height/2)-INPUT_BOX_HEIGHT*2)]
        )

        average_wpm_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            average_wpm,
            average_wpm_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)-INPUT_BOX_HEIGHT*1.5)],
            [(screen_width/2), ((screen_height/2)-INPUT_BOX_HEIGHT*1)]
        )

        last_10_wpm_average_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            last_10_average_wpm,
            last_10_average_wpm_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, (screen_height/2)-INPUT_BOX_HEIGHT*0.5],
            [(screen_width/2), (screen_height/2)]
        )

        highest_wpm_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            highest_wpm,
            highest_wpm_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, (screen_height/2)+INPUT_BOX_HEIGHT*0.5],
            [(screen_width/2), (screen_height/2)+INPUT_BOX_HEIGHT*1]
        )

        total_keypresses_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            total_keypresses,
            total_keypresses_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)+INPUT_BOX_HEIGHT*1.5)],
            [(screen_width/2), ((screen_height/2)+INPUT_BOX_HEIGHT*2)]
        )

        join_date_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            join_date,
            join_date_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2.5)],
            [(screen_width/2), ((screen_height/2)+INPUT_BOX_HEIGHT*3)]
        )

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

        level_button.init_box()
        level_button.init_center_text()
        level_button.blit_box(BLACK)
        level_button.blit_center_text()

        average_wpm_button.init_box()
        average_wpm_button.init_center_text()
        average_wpm_button.blit_box(BLACK)
        average_wpm_button.blit_center_text()

        last_10_wpm_average_button.init_center_text()
        last_10_wpm_average_button.blit_center_text()

        highest_wpm_button.init_box()
        highest_wpm_button.init_center_text()
        highest_wpm_button.blit_box(BLACK)
        highest_wpm_button.blit_center_text()

        total_keypresses_button.init_center_text()
        total_keypresses_button.blit_center_text()

        join_date_button.init_box()
        join_date_button.init_center_text()
        join_date_button.blit_box(BLACK)
        join_date_button.blit_center_text()

        back_button.init_box()
        back_button.init_center_text()
        back_button.blit_box(BLACK)
        back_button.blit_center_text()


    #################################

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
            
                if back_button.get_box().collidepoint(event.pos):
                    return 0

            if event.type == QUIT:
                return 1

        back_box_thickness = SELECTED_THICKNESS if back_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS

        pygame.display.flip()
        n+=1



if __name__ == '__main__':
    statistics_screen(Account('tom','bed'))
    pygame.quit() # THIS MIGHT NEED TO BE REMOVED WHEN WE GO FROM SCREEN TO SCREEN AND ONLY WHEN YOU ACTUALLY QUIT

    ###