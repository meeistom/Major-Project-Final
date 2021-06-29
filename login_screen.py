# Filename: login_screen.py
# Author: Tom Bednarek
# Date: May 2021

# MAYBE STOP PEOPLE BEING ABLE TO TYPE ':' HERE AND NOT EVEN HAVE TO WORRY ABOUT IT LATER

# HOLD BACKSPACE - pygame.key.get_pressed() isn't working for some reason
# THIS IS VERY HARD
# MAKE IT COUNT THE NUMBER OF KEYSPRESSED WHILE NOT LOGGED IN THEN ADD IT TO THE ACCOUNT LOGGED INTO OR CREATED


import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()

def login_screen():

    ###### CONSTANTS ######

    PROGRAM_NAME = 'Digit Reboot'
    TITLE_FONT = 'Courier New'
    TEXT_FONT = 'Courier New'
    USERNAME = 'Username'
    PASSWORD = 'Password'
    REGISTER = 'Register'
    CENSOR = '●' # chr(9679)
    LOGIN = 'Login'
    SHOW = 'show'
    HIDE = 'hide'
    WHITE = (255, 255, 255)
    LIGHT_GREY = (175, 175, 175)
    BLACK = (0, 0, 0)
    TITLE_FONT_SIZE = 60
    TEXT_FONT_SIZE = 24
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    REGISTER_BOX_WIDTH = 200
    SELECTED_THICKNESS = 2
    DESELECTED_THICKNESS = 1
    SHOW_PASSWORD_WIDTH = SHOW_PASSWORD_HEIGHT = INPUT_BOX_HEIGHT
    LOGO = pygame.image.load("digit_reboot_logo.png")
    UPPER_DICT = {
        '`':'~','1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')','-':'_',
        '=':'+','q':'Q','w':'W','e':'E','r':'R','t':'T','y':'Y','u':'U','i':'I','o':'O','p':'P','[':'{',
        ']':'}','\\':'|','a':'A','s':'S','d':'D','f':'F','g':'G','h':'H','j':'J','k':'K','l':'L',';':':',
        '\'':'"','z':'Z','x':'X','c':'C','v':'V','b':'B','n':'N','m':'M',',':'<','.':'>','/':'?',' ':' '
    }

    ACCOUNTS = 'accounts.txt'
    DELIMITER = '≡' # chr(8801)

    ###

    ###### DISPLAY ######

    ### DISPLAY LOOP ###

    valid_characters = [x for x in range(0,127)]
    screen_width = 1366
    screen_height = round(screen_width*9/16)
    show_password = SHOW
    username_box_thickness = DESELECTED_THICKNESS
    password_box_thickness = DESELECTED_THICKNESS
    login_box_thickness = DESELECTED_THICKNESS
    register_box_thickness = DESELECTED_THICKNESS
    show_password_box_thickness = DESELECTED_THICKNESS
    username_active = False
    password_active = False
    login_active = False
    show_password_active = False
    censor_on = True
    n=0
    pressed=[]
    pressed_dict = {}
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
            PROGRAM_NAME,
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

        try:
            username = username_box.get_text()
        except NameError:
            username = ''
        
        try:
            password = password_box.get_text()
        except NameError:
            password = ''

        username_box = InputBox(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            username,
            username_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)-INPUT_BOX_HEIGHT*2)],
            [((screen_width/2)-INPUT_BOX_WIDTH/2)+TEXT_FONT_SIZE, ((screen_height/2)-INPUT_BOX_HEIGHT*1.5)-TEXT_FONT_SIZE/2]
        )

        password_box = InputBox(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            password,
            password_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, (screen_height/2)],
            [((screen_width/2)-INPUT_BOX_WIDTH/2)+TEXT_FONT_SIZE, ((screen_height/2)+INPUT_BOX_HEIGHT/2)-TEXT_FONT_SIZE/2]
        )

        login_button = Button(
            INPUT_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            LOGIN,
            login_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)-INPUT_BOX_WIDTH/2, ((screen_height/2)+INPUT_BOX_HEIGHT*2)],
            [(screen_width/2), ((screen_height/2)+INPUT_BOX_HEIGHT*2.5)]
        )

        register_button = Button(
            REGISTER_BOX_WIDTH, 
            INPUT_BOX_HEIGHT,
            REGISTER,
            register_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [screen_width-REGISTER_BOX_WIDTH-50, screen_height-INPUT_BOX_HEIGHT-50],
            [screen_width-REGISTER_BOX_WIDTH/2-50, (screen_height-INPUT_BOX_HEIGHT-50+TEXT_FONT_SIZE*1.5)]
        )

        show_password_button = Button(
            SHOW_PASSWORD_WIDTH, 
            SHOW_PASSWORD_HEIGHT,
            show_password,
            show_password_box_thickness,
            BLACK,
            screen,
            TEXT_FONT,
            TEXT_FONT_SIZE,
            [(screen_width/2)+INPUT_BOX_WIDTH/2+INPUT_BOX_HEIGHT/2, (screen_height/2)],
            [(screen_width/2)+INPUT_BOX_WIDTH/2+INPUT_BOX_HEIGHT, (screen_height/2)+SHOW_PASSWORD_HEIGHT/2]
        )

        username_box.init_box()
        username_box.init_side_text()
        username_box.blit_box(BLACK)
        username_box.blit_side_text(False)
        username_box.blit_watermark(USERNAME, LIGHT_GREY)
        if username_active:
            username_box.init_flash(DESELECTED_THICKNESS)
            username_box.blit_flash(on())

        password_box.init_box()
        password_box.init_side_text()
        password_box.blit_box(BLACK)
        password_box.blit_side_text(censor_on, CENSOR)
        password_box.blit_watermark(PASSWORD, LIGHT_GREY)
        if password_active:
            password_box.init_flash(DESELECTED_THICKNESS)
            password_box.blit_flash(on())

        login_button.init_box()
        login_button.init_center_text()
        login_button.blit_box(BLACK)
        login_button.blit_center_text()

        register_button.init_box()
        register_button.init_center_text()
        register_button.blit_box(BLACK)
        register_button.blit_center_text()

        show_password_button.init_box()
        show_password_button.init_center_text()
        show_password_button.blit_box(BLACK)
        show_password_button.blit_center_text()

    #################################

        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:
                
                if username_box.get_box().collidepoint(event.pos):
                    username_active = not username_active
                    password_active = False
                    
                elif password_box.get_box().collidepoint(event.pos):
                    password_active = not password_active
                    username_active = False

                elif login_button.get_box().collidepoint(event.pos):
                    if login(file_to_dict(ACCOUNTS, DELIMITER), username_box.get_text(), password_box.get_text()):
                        return [0, username_box.get_text()]
            
                elif register_button.get_box().collidepoint(event.pos):
                    return [1]

                elif show_password_button.get_box().collidepoint(event.pos):
                    show_password_active = not show_password_active
                    if show_password_active:
                        show_password = HIDE
                    else:
                        show_password = SHOW
                    censor_on = not censor_on
                    
                else:
                    username_active = False
                    password_active = False

            if event.type == QUIT:
                return [2]

        username_box_thickness = SELECTED_THICKNESS if username_active or username_box.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        password_box_thickness = SELECTED_THICKNESS if password_active or password_box.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        login_box_thickness = SELECTED_THICKNESS if login_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        register_box_thickness = SELECTED_THICKNESS if register_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        show_password_box_thickness = SELECTED_THICKNESS if (show_password_active or show_password_button.get_box().collidepoint(pygame.mouse.get_pos())) else DESELECTED_THICKNESS
    
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return [2]

        if username_active:

            lst = [key for key in pressed_dict.keys()]

            for key in lst:
                if not pressed[ord(key)]:
                    del pressed_dict[key]

            for char in valid_characters:

                if keys[char] and char != 8 and pressed[char]:

                    if timer(pressed_dict[chr(char)]):
                        if keys[K_RSHIFT] or keys[K_LSHIFT]:
                            username_box.add_letter(UPPER_DICT[chr(char)], round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                        else:
                            username_box.add_letter(chr(char), round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                
                elif keys[char] and char != 8 and not pressed[char]:
                    if keys[K_RSHIFT] or keys[K_LSHIFT]:
                        username_box.add_letter(UPPER_DICT[chr(char)], round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                    else:
                        username_box.add_letter(chr(char), round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                    pressed_dict[chr(char)] = time.time()

                elif keys[char] and char == 8 and pressed[char]:
                    if timer(pressed_dict[chr(char)]):
                        username_box.remove_letter()
                
                elif keys[char] and char == 8 and not pressed[char]:
                    username_box.remove_letter()
                    pressed_dict[chr(char)] = time.time()

        elif password_active:

            lst = [key for key in pressed_dict.keys()]

            for key in lst:
                if not pressed[ord(key)]:
                    del pressed_dict[key]

            for char in valid_characters:

                if keys[char] and char != 8 and pressed[char]:

                    if timer(pressed_dict[chr(char)]):
                        if keys[K_RSHIFT] or keys[K_LSHIFT]:
                            password_box.add_letter(UPPER_DICT[chr(char)], round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                        else:
                            password_box.add_letter(chr(char), round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                
                elif keys[char] and char != 8 and not pressed[char]:
                    if keys[K_RSHIFT] or keys[K_LSHIFT]:
                        password_box.add_letter(UPPER_DICT[chr(char)], round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                    else:
                        password_box.add_letter(chr(char), round(TEXT_FONT_SIZE*9/16+TEXT_FONT_SIZE))
                    pressed_dict[chr(char)] = time.time()

                elif keys[char] and char == 8 and pressed[char]:
                    if timer(pressed_dict[chr(char)]):
                        password_box.remove_letter()
                
                elif keys[char] and char == 8 and not pressed[char]:
                    password_box.remove_letter()
                    pressed_dict[chr(char)] = time.time()

        pressed = keys

        pygame.display.flip()
        n+=1



if __name__ == '__main__':
    login_screen()
    pygame.quit() # THIS MIGHT NEED TO BE REMOVED WHEN WE GO FROM SCREEN TO SCREEN AND ONLY WHEN YOU ACTUALLY QUIT

    ###