# Filename: wpm_test_screen.py
# Author: Tom Bednarek
# Date: May, June 2021

import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()



def wpm_test_screen(account):

    ###### CONSTANTS ######

    PROGRAM_NAME = 'Digit Reboot'
    TEXT_FONT = 'Courier New'
    BACK = 'Back'
    WPM_TEST_TEXT = 'WPM Test'
    WHITE = (255, 255, 255)
    LIGHT_GREY = (175, 175, 175)
    BLACK = (0, 0, 0)
    TEXT_FONT_SIZE = 24
    BACK_BOX_WIDTH = WPM_BOX_WIDTH = 200
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    SELECTED_THICKNESS = 2
    DESELECTED_THICKNESS = 1
    TOP_BUFFER = 50
    SIDE_BUFFER = 50
    LOGO = pygame.image.load("digit_reboot_logo.png")
    UPPER_DICT = {
        '`':'~','1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')','-':'_',
        '=':'+','q':'Q','w':'W','e':'E','r':'R','t':'T','y':'Y','u':'U','i':'I','o':'O','p':'P','[':'{',
        ']':'}','\\':'|','a':'A','s':'S','d':'D','f':'F','g':'G','h':'H','j':'J','k':'K','l':'L',';':':',
        '\'':'"','z':'Z','x':'X','c':'C','v':'V','b':'B','n':'N','m':'M',',':'<','.':'>','/':'?',' ':' ',
        '\r':'\n','\t':'\t'
    }

    DICTIONARY = 'common_words.txt'

    DARK_GREEN = (39, 78, 19)
    LIGHT_GREEN = (147, 196, 125)
    DARK_YELLOW = (127, 96, 0)
    LIGHT_YELLOW = (255, 217, 96)
    DARK_RED = (102, 0, 0)
    LIGHT_RED = (224, 102, 102)

    DARK_COLOURS = [DARK_GREEN, DARK_YELLOW, DARK_RED]
    LIGHT_COLOURS = [LIGHT_GREEN, LIGHT_YELLOW, LIGHT_RED]

    valid_characters = [x for x in range(0,127)]
    screen_width = 1366
    screen_height = round(screen_width*9/16)
    input_text = ''
    WPM_test_active = True
    WPM_text_box_thickness = DESELECTED_THICKNESS
    back_box_thickness = DESELECTED_THICKNESS
    WPM_box_thickness = DESELECTED_THICKNESS
    WPM_test_box_thickness = DESELECTED_THICKNESS
    wrong_indexes = set()
    pressed=[]
    pressed_dict = {}
    check = False
    start_time_check = False
    input_box_width = screen_width-100
    input_box_height = screen_height-200

    WPM_text = ''

    words = file_to_lst(DICTIONARY)
    for i in range(100):
        WPM_text += random.choice(words)+' '

    WPM_text = WPM_text.strip()

    screen = pygame.display.set_mode([screen_width, screen_height], RESIZABLE)
    pygame.display.set_caption(PROGRAM_NAME)
    pygame.display.set_icon(LOGO)

    screen.fill(WHITE)

    back_button, runs = beginning_blit(
        screen_width,
        screen_height,
        screen,
        WHITE,
        BLACK,
        LIGHT_GREY,
        BACK_BOX_WIDTH,
        input_box_width,
        INPUT_BOX_HEIGHT,
        BACK,
        back_box_thickness,
        TEXT_FONT,
        TEXT_FONT_SIZE,
        WPM_text,
        WPM_text_box_thickness,
        WPM_test_box_thickness,
        INPUT_BOX_WIDTH,
        WPM_TEST_TEXT,
        TOP_BUFFER,
        SIDE_BUFFER
    )

    running = True

    letters = []

    while running:

        previous_screen_width = screen_width
        previous_screen_height = screen_height

        screen_width, screen_height = screen.get_size()

        input_box_width = screen_width-100
        input_box_height = screen_height-150-INPUT_BOX_HEIGHT

        if previous_screen_width != screen_width or previous_screen_height != screen_height:
            back_button, runs = beginning_blit(
                screen_width,
                screen_height,
                screen,
                WHITE,
                BLACK,
                LIGHT_GREY,
                BACK_BOX_WIDTH,
                input_box_width,
                INPUT_BOX_HEIGHT,
                BACK,
                back_box_thickness,
                TEXT_FONT,
                TEXT_FONT_SIZE,
                WPM_text,
                WPM_text_box_thickness,
                WPM_test_box_thickness,
                INPUT_BOX_WIDTH,
                WPM_TEST_TEXT,
                TOP_BUFFER,
                SIDE_BUFFER
            )

            letters = []

            for i in range(len(input_text)):
                try:
                    x_pos, y_pos = blitting_letters(runs, input_text[0:i], TEXT_FONT_SIZE, letters, WPM_text, wrong_indexes, screen, TEXT_FONT, DARK_COLOURS, LIGHT_COLOURS, SIDE_BUFFER, TOP_BUFFER)
                except TypeError:
                    pass

        try:
            input_text = WPM_text_box.get_text()
        except NameError:
            input_text = ''

        WPM_text_box = InputBox(
            input_box_width,
            input_box_height,
            input_text,
            WPM_text_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [SIDE_BUFFER,TOP_BUFFER],
            [SIDE_BUFFER+TEXT_FONT_SIZE,TOP_BUFFER+TEXT_FONT_SIZE]
        )

        correct_cpm = 0
        for i in range(len(input_text)):
            if input_text[i] == WPM_text[i]:
                correct_cpm+=1

        if start_time_check:
            x = temp_WPM_calculator(start_time, correct_cpm, AVERAGE_WORD_LENGTH)
        else:
            x=0

        WPM_box = Button(
            WPM_BOX_WIDTH,
            INPUT_BOX_HEIGHT,
            f'WPM: {x}',
            WPM_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [SIDE_BUFFER, screen_height-INPUT_BOX_HEIGHT-TOP_BUFFER],
            [SIDE_BUFFER+BACK_BOX_WIDTH/2, screen_height-INPUT_BOX_HEIGHT/2-TOP_BUFFER]

        )

        WPM_box.init_box()
        WPM_box.init_center_text()
        WPM_box.blit_box(WHITE, thickness=None)
        WPM_box.blit_box(BLACK)
        WPM_box.blit_center_text()



        WPM_text_box.init_box()
        if not WPM_test_active:
            WPM_text_box.blit_box(WHITE, thickness=WPM_text_box_thickness+1)
        WPM_text_box.blit_box(BLACK)

        back_button.init_box()
        if not back_button.get_box().collidepoint(pygame.mouse.get_pos()):
            back_button.blit_box(WHITE, thickness=back_box_thickness+1)
        back_button.blit_box(BLACK, thickness=back_box_thickness)



        for i in range(len(input_text)):
            if input_text[i] != WPM_text[i]:
                wrong_indexes.add(i)



        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:

                if WPM_text_box.get_box().collidepoint(event.pos):

                    WPM_test_active = not WPM_test_active
                
                elif back_button.get_box().collidepoint(event.pos):
                    return [1]
                
                else:

                    WPM_test_active = False
            
            elif event.type == QUIT:
                return [2]

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return [2]

        if WPM_test_active:

            lst = [key for key in pressed_dict.keys()]

            for key in lst:
                if not pressed[ord(key)]:
                    del pressed_dict[key]

            for char in valid_characters:



                if keys[char] and char != 8 and not pressed[char]:
                    if keys[K_RSHIFT] or keys[K_LSHIFT]:
                        WPM_text_box.add_letter(UPPER_DICT[chr(char)], len(WPM_text))
                    else:
                        WPM_text_box.add_letter(chr(char), len(WPM_text))

                    if not start_time_check:
                        start_time = time.time()
                        start_time_check = True
                    
                    account.increment_total_keypresses()



                elif keys[char] and char == 8 and pressed[char]:
                    if timer(pressed_dict[chr(char)]):
                        WPM_text_box.remove_letter()

                        if len(input_text) == 0:
                            index = 0
                        else:
                            index = len(input_text)-1

                        letter=Letter(
                            WPM_text[index],
                            LIGHT_GREY,
                            WHITE,
                            screen,
                            TEXT_FONT,
                            TEXT_FONT_SIZE,
                            [x_pos, y_pos]
                        )

                        letter.init_highlight()
                        letter.init_letter()
                        letter.blit_highlight()
                        letter.blit_letter()

                        letters.pop()



                if keys[char] and char == 8 and not pressed[char]:
                    WPM_text_box.remove_letter()
                    pressed_dict[chr(char)] = time.time()

                    if len(input_text) == 0:
                            index = 0
                    else:
                        index = len(input_text)-1

                    letter=Letter(
                        WPM_text[index],
                        LIGHT_GREY,
                        WHITE,
                        screen,
                        TEXT_FONT,
                        TEXT_FONT_SIZE,
                        [x_pos, y_pos]
                    )

                    letter.init_highlight()
                    letter.init_letter()
                    letter.blit_highlight()
                    letter.blit_letter()

                    letters.pop()

                    account.increment_total_keypresses()



        pressed = keys

        input_text = WPM_text_box.get_text()

        WPM_text_box_thickness = SELECTED_THICKNESS if WPM_test_active or WPM_text_box.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        back_box_thickness = SELECTED_THICKNESS if back_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS

        try:
            x_pos, y_pos = blitting_letters(runs, input_text, TEXT_FONT_SIZE, letters, WPM_text, wrong_indexes, screen, TEXT_FONT, DARK_COLOURS, LIGHT_COLOURS, SIDE_BUFFER, TOP_BUFFER)
        except TypeError:
            pass

        pygame.display.flip()

        if check:
            total = 0
            for i in range(len(input_text)):
                if input_text[i] == WPM_text[i]:
                    total += 1

            return [0, x, total*100//len(WPM_text)]

        if len(input_text) == len(WPM_text):
            check = True


if __name__ == '__main__':
    wpm_test_screen(Account('tom','bed'))
    pygame.quit()
