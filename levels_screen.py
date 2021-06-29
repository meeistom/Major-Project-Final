# Filename: levels_screen.py
# Author: Tom Bednarek
# Date: May, June 2021

import pygame
from pygame.locals import *
from digit_reboot_classes import *
from digit_reboot_functions import *
pygame.init()


def levels_screen(account):

    ###### CONSTANTS ######

    PROGRAM_NAME = 'Digit Reboot'
    KEYBOARD_FONT = 'Calibri'
    ARROW_FONT = 'Times New Roman'
    TEXT_FONT = 'Courier New'
    BACK = 'Back'
    FILL_CHAR = '0'
    WHITE = (255, 255, 255)
    LIGHT_BLUE = (0, 241, 255)
    LIGHT_GREY = (175, 175, 175)
    BLACK = (0, 0, 0)
    TEXT_FONT_SIZE = 20
    KEYBOARD_FONT_SIZE = 15
    BACK_BOX_WIDTH = WPM_BOX_WIDTH = 200
    INPUT_BOX_WIDTH = TEXT_FONT_SIZE**2
    INPUT_BOX_HEIGHT = TEXT_FONT_SIZE*3
    SELECTED_THICKNESS = 2
    DESELECTED_THICKNESS = 1
    TOP_BUFFER = 25
    SIDE_BUFFER = 25
    KEY_WIDTH = KEY_HEIGHT = 55
    KEY_SPACING = 5
    RADIUS = 10
    TEXT_BUFFER = 10
    LOGO = pygame.image.load("digit_reboot_logo.png")

    LEFT_HAND = pygame.image.load('left_hand.png')
    RIGHT_HAND = pygame.image.load('right_hand.png')
    LEFT_BLUE_HAND = pygame.image.load('left_blue_hand.png')
    RIGHT_BLUE_HAND = pygame.image.load('right_blue_hand.png') #246, 334

    LEFT_HAND = pygame.transform.smoothscale(LEFT_HAND, (int(LEFT_HAND.get_width()/1.2), int(LEFT_HAND.get_height()/1.2)))
    RIGHT_HAND = pygame.transform.smoothscale(RIGHT_HAND, (int(RIGHT_HAND.get_width()/1.2), int(RIGHT_HAND.get_height()/1.2))) 
    LEFT_BLUE_HAND = pygame.transform.smoothscale(LEFT_BLUE_HAND, (int(LEFT_BLUE_HAND.get_width()/1.2), int(LEFT_BLUE_HAND.get_height()/1.2))) 
    RIGHT_BLUE_HAND = pygame.transform.smoothscale(RIGHT_BLUE_HAND, (int(RIGHT_BLUE_HAND.get_width()/1.2), int(RIGHT_BLUE_HAND.get_height()/1.2))) 

    UPPER_DICT = {
        '`':'~','1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')','-':'_',
        '=':'+','q':'Q','w':'W','e':'E','r':'R','t':'T','y':'Y','u':'U','i':'I','o':'O','p':'P','[':'{',
        ']':'}','\\':'|','a':'A','s':'S','d':'D','f':'F','g':'G','h':'H','j':'J','k':'K','l':'L',';':':',
        '\'':'"','z':'Z','x':'X','c':'C','v':'V','b':'B','n':'N','m':'M',',':'<','.':'>','/':'?',' ':' ',
        '\r':'\n','\t':'\t'
    }

    LOWER_DICT = {
        '~':'`','!':'1','@':'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8','(':'9',')':'0','_':'-',
        '+':'=','Q':'q','W':'w','E':'e','R':'r','T':'t','Y':'y','U':'u','I':'i','O':'o','P':'p','{':'[',
        '}':']','|':'\\','A':'a','S':'s','D':'d','F':'f','G':'g','H':'h','J':'j','K':'k','L':'l',':':';',
        '"':'\'','Z':'z','X':'x','C':'c','V':'v','B':'b','N':'n','M':'m','<':',','>':'.','?':'/',' ':' ',
        '\n':'\r','\t':'\t'
    }

    NUMBER_ROW_KEYS = [['`','~'],['1','!'],['2','@'],['3','#'],['4','$'],['5','%'],['6','^'],['7','&'],['8','*'],['9','('],['0',')'],['-','_'],['=','+'],['backspace']]
    TOP_ROW_KEYS = [['tab'],['Q'],['W'],['E'],['R'],['T'],['Y'],['U'],['I'],['O'],['P'],['[','{'],[']','}'],['\\','|']]
    HOME_ROW_KEYS = [['caps lock'],['A'],['S'],['D'],['F'],['G'],['H'],['J'],['K'],['L'],[';',':'],['\'','"'],['enter']]
    BOTTOM_ROW_KEYS = [['shift'],['Z'],['X'],['C'],['V'],['B'],['N'],['M'],[',','<'],['.','>'],['/','?'],['shift']]
    FUNCTION_ROW_KEYS = [['ctrl'],['fn'],['win'],['alt'],['spacebar'],['alt'],['ctrl'],['◄'],['▲'],['▼'],['►']]

    LETTER_TO_INDEX_DICT = {
        '`':1,'1':2,'2':3,'3':4,'4':5,'5':6,'6':7,'7':8,'8':9,'9':10,
        '0':11,'-':12,'=':13,'backspace':14,'tab':15,'Q':16,'W':17,'E':18,'R':19,'T':20,
        'Y':21,'U':22,'I':23,'O':24,'P':25,'[':26,']':27,'\\':28,'caps lock':29,'A':30,
        'S':31,'D':32,'F':33,'G':34,'H':35,'J':36,'K':37,'L':38,';':39,'\'':40,
        'enter':41,'l_shift':42,'Z':43,'X':44,'C':45,'V':46,'B':47,'N':48,'M':49,',':50,
        '.':51,'/':52,'r_shift':53,'l_ctrl':54,'fn':55,'win':56,'l_alt':57,' ':58,'r_alt':59,'r_ctrl':60,
        'left':61,'up':62,'down':63,'right':64
    }

    DARK_GREEN = (39, 78, 19)
    LIGHT_GREEN = (147, 196, 125)
    DARK_YELLOW = (127, 96, 0)
    LIGHT_YELLOW = (255, 217, 96)
    DARK_RED = (102, 0, 0)
    LIGHT_RED = (224, 102, 102)

    DARK_COLOURS = [DARK_GREEN, DARK_YELLOW, DARK_RED]
    LIGHT_COLOURS = [LIGHT_GREEN, LIGHT_YELLOW, LIGHT_RED]

    R_SHIFT_INDEX = [1,2,3,4,5,6,16,17,18,19,20,30,31,32,33,34,43,44,45,46,47]
    L_SHIFT_INDEX = [7,8,9,10,11,12,13,21,22,23,24,25,26,27,28,35,36,37,38,39,40,48,49,50,51,52]

    LEFT_PINKY_INDEX = [1,2,16,30,42,43]
    LEFT_RING_INDEX = [3,17,31,44]
    LEFT_MIDDLE_INDEX = [4,18,32,45]
    LEFT_INDEX_INDEX = [5,6,19,20,33,34,46,47]
    LEFT_THUMB_INDEX = [58] # add cases where the previous letter typed in right or left

    RIGHT_THUMB_INDEX = [58] # add cases where the previous letter typed in right or left
    RIGHT_INDEX_INDEX = [7,8,21,22,35,36,48,49]
    RIGHT_MIDDLE_INDEX = [9,23,37,50]
    RIGHT_RING_INDEX = [10,24,38,51]
    RIGHT_PINKY_INDEX = [11,12,13,14,25,26,27,28,39,40,52,53]

    LEVELS = 'levels.txt'

    valid_characters = [x for x in range(0,127)]
    screen_width = 1366
    screen_height = round(screen_width*9/16)
    levels = file_to_lst(LEVELS)
    try:
        level_text = levels[account.get_level()]
    except IndexError:
        account.set_level(len(levels)-1)
        level_text = levels[account.get_level()]

    LEVEL_TEXT = f'Level {fill_blanks(str(account.get_level()+1), FILL_CHAR)}'

    input_text = ''
    level_active = True
    level_text_box_thickness = DESELECTED_THICKNESS
    back_box_thickness = DESELECTED_THICKNESS
    WPM_box_thickness = DESELECTED_THICKNESS
    WPM_test_box_thickness = DESELECTED_THICKNESS
    wrong_indexes = set()
    pressed=[]
    pressed_dict = {}
    check = False
    start_time_check = False
    input_box_width = screen_width-100
    input_box_height = screen_height/2-100

    active_lst = [False for i in range(len(NUMBER_ROW_KEYS)+len(TOP_ROW_KEYS)+len(HOME_ROW_KEYS)+len(BOTTOM_ROW_KEYS)+len(FUNCTION_ROW_KEYS)+1)]

    screen = pygame.display.set_mode([screen_width, screen_height], RESIZABLE)
    pygame.display.set_caption(PROGRAM_NAME)
    pygame.display.set_icon(LOGO)

    screen.fill(WHITE)


    x=0
    y=0

    keys, keyboard_width, keyboard_height, active_lst = create_keyboard(KEYBOARD_FONT,ARROW_FONT,KEYBOARD_FONT_SIZE,DESELECTED_THICKNESS,SELECTED_THICKNESS,BLACK,LIGHT_GREY,LIGHT_BLUE,WHITE,KEY_WIDTH,KEY_HEIGHT,KEY_SPACING,RADIUS,NUMBER_ROW_KEYS,TOP_ROW_KEYS,HOME_ROW_KEYS,BOTTOM_ROW_KEYS,FUNCTION_ROW_KEYS,screen,TEXT_BUFFER,[screen_width/2-x,screen_height-y-50],active_lst)

    screen.fill(WHITE)

    back_button, runs = beginning_blit(screen_width,screen_height,screen,WHITE,BLACK,LIGHT_GREY,BACK_BOX_WIDTH,input_box_width,INPUT_BOX_HEIGHT,BACK,back_box_thickness,TEXT_FONT,TEXT_FONT_SIZE,level_text,level_text_box_thickness,WPM_test_box_thickness,INPUT_BOX_WIDTH,LEVEL_TEXT,TOP_BUFFER,SIDE_BUFFER)

    running = True

    letters = []

    while running:

        previous_screen_width = screen_width
        previous_screen_height = screen_height

        screen_width, screen_height = screen.get_size()

        input_box_width = screen_width-100
        input_box_height = screen_height-TOP_BUFFER*4-keyboard_height-INPUT_BOX_HEIGHT

        if previous_screen_width != screen_width or previous_screen_height != screen_height:
            back_button, runs = beginning_blit(screen_width,screen_height,screen,WHITE,BLACK,LIGHT_GREY,BACK_BOX_WIDTH,input_box_width,INPUT_BOX_HEIGHT,BACK,back_box_thickness,TEXT_FONT,TEXT_FONT_SIZE,level_text,level_text_box_thickness,WPM_test_box_thickness,INPUT_BOX_WIDTH,LEVEL_TEXT,TOP_BUFFER,SIDE_BUFFER)

            letters = []

            for i in range(len(input_text)):
                try:
                    x_pos, y_pos = blitting_letters(runs, input_text[0:i], TEXT_FONT_SIZE, letters, level_text, wrong_indexes, screen, TEXT_FONT, DARK_COLOURS, LIGHT_COLOURS, TOP_BUFFER, SIDE_BUFFER)
                except TypeError:
                    pass


        try:
            x = keyboard_width/2
            y = keyboard_height
        except NameError:
            x=0
            y=0

        active_lst = [False for i in range(len(NUMBER_ROW_KEYS)+len(TOP_ROW_KEYS)+len(HOME_ROW_KEYS)+len(BOTTOM_ROW_KEYS)+len(FUNCTION_ROW_KEYS)+1)]
        index = len(input_text)

        try:
            if level_text[index] in UPPER_DICT.keys():

                if level_text[index].isalpha():
                    active_lst[LETTER_TO_INDEX_DICT[UPPER_DICT[level_text[index]]]] = True
                else:
                    active_lst[LETTER_TO_INDEX_DICT[level_text[index]]] = True

            elif level_text[index] in UPPER_DICT.values():

                if level_text[index].isalpha():
                    active_lst[LETTER_TO_INDEX_DICT[level_text[index]]] = True

                    if LETTER_TO_INDEX_DICT[level_text[index]] in L_SHIFT_INDEX:
                        active_lst[42] = True

                    elif LETTER_TO_INDEX_DICT[level_text[index]] in R_SHIFT_INDEX:
                        active_lst[53] = True

                else:
                    active_lst[LETTER_TO_INDEX_DICT[LOWER_DICT[level_text[index]]]] = True
                    if LETTER_TO_INDEX_DICT[LOWER_DICT[level_text[index]]] in L_SHIFT_INDEX:
                        active_lst[42] = True

                    elif LETTER_TO_INDEX_DICT[LOWER_DICT[level_text[index]]] in R_SHIFT_INDEX:
                        active_lst[53] = True

        except IndexError:
            pass

        keys, keyboard_width, keyboard_height, active_lst = create_keyboard(KEYBOARD_FONT,ARROW_FONT,KEYBOARD_FONT_SIZE,DESELECTED_THICKNESS,SELECTED_THICKNESS,BLACK,LIGHT_GREY,LIGHT_BLUE,WHITE,KEY_WIDTH,KEY_HEIGHT,KEY_SPACING,RADIUS,NUMBER_ROW_KEYS,TOP_ROW_KEYS,HOME_ROW_KEYS,BOTTOM_ROW_KEYS,FUNCTION_ROW_KEYS,screen,TEXT_BUFFER,[screen_width/2-x,screen_height-y-TOP_BUFFER*2-INPUT_BOX_HEIGHT],active_lst)

        screen.blit(LEFT_HAND, [screen_width/2-x-LEFT_HAND.get_width()-20,screen_height-LEFT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT])
        screen.blit(RIGHT_HAND, [screen_width/2+x+20,screen_height-RIGHT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT])      
        
        for i in range(len(active_lst)):
            if active_lst[i] == True:
                if i in LEFT_PINKY_INDEX:
                    screen.blit(LEFT_BLUE_HAND, [screen_width/2-x-LEFT_HAND.get_width()-20,screen_height-LEFT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[0,0,34,95]) # left pinky
                elif i in LEFT_RING_INDEX:
                    screen.blit(LEFT_BLUE_HAND, [screen_width/2-x-LEFT_HAND.get_width()-20+36,screen_height-LEFT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[36,0,34,70]) # left ring
                elif i in LEFT_MIDDLE_INDEX:    
                    screen.blit(LEFT_BLUE_HAND, [screen_width/2-x-LEFT_HAND.get_width()-20+70,screen_height-LEFT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[70,0,34,50]) # left middle
                elif i in LEFT_INDEX_INDEX:
                    screen.blit(LEFT_BLUE_HAND, [screen_width/2-x-LEFT_HAND.get_width()-20+115,screen_height-LEFT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[115,0,34,70]) # left index

                elif i in RIGHT_THUMB_INDEX: # WHEN SPACE IT DOESNT SHOW UP ON RIGHT THUMB CAUSE ELIF
                    screen.blit(RIGHT_BLUE_HAND, [screen_width/2+x+20,screen_height-RIGHT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[0,0,34,190]) # right thumb
                elif i in RIGHT_INDEX_INDEX:
                    screen.blit(RIGHT_BLUE_HAND, [screen_width/2+x+20+55,screen_height-RIGHT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[55,0,34,70]) # right index
                elif i in RIGHT_MIDDLE_INDEX:
                    screen.blit(RIGHT_BLUE_HAND, [screen_width/2+x+20+100,screen_height-RIGHT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[100,0,34,50]) # right middle
                elif i in RIGHT_RING_INDEX:
                    screen.blit(RIGHT_BLUE_HAND, [screen_width/2+x+20+134,screen_height-RIGHT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[134,0,34,70]) # right ring
                elif i in RIGHT_PINKY_INDEX:
                    screen.blit(RIGHT_BLUE_HAND, [screen_width/2+x+20+170,screen_height-RIGHT_HAND.get_height()-TOP_BUFFER*2-INPUT_BOX_HEIGHT],[170,0,34,95]) # right pinky

        try:
            input_text = level_text_box.get_text()
        except NameError:
            input_text = ''

        level_text_box = InputBox(input_box_width,input_box_height,input_text,level_text_box_thickness,BLACK,screen,TEXT_FONT,TEXT_FONT_SIZE,[SIDE_BUFFER,TOP_BUFFER],[SIDE_BUFFER+TEXT_FONT_SIZE,TOP_BUFFER+TEXT_FONT_SIZE])

        correct_cpm = 0
        for i in range(len(input_text)):
            if input_text[i] == level_text[i]:
                correct_cpm+=1

        if start_time_check:
            x = temp_WPM_calculator(start_time, correct_cpm, AVERAGE_WORD_LENGTH)
        else:
            x=0

        WPM_box = Button(WPM_BOX_WIDTH,INPUT_BOX_HEIGHT,f'WPM: {x}',WPM_box_thickness,BLACK,screen,TEXT_FONT,TEXT_FONT_SIZE,[SIDE_BUFFER, screen_height-INPUT_BOX_HEIGHT-TOP_BUFFER],[SIDE_BUFFER+BACK_BOX_WIDTH/2, screen_height-INPUT_BOX_HEIGHT/2-TOP_BUFFER])

        WPM_box.init_box()
        WPM_box.init_center_text()
        WPM_box.blit_box(WHITE, thickness=None)
        WPM_box.blit_box(BLACK)
        WPM_box.blit_center_text()

        level_text_box.init_box()
        if not level_active:
            level_text_box.blit_box(WHITE, thickness=level_text_box_thickness+1)
        level_text_box.blit_box(BLACK)

        back_button.init_box()
        if not back_button.get_box().collidepoint(pygame.mouse.get_pos()):
            back_button.blit_box(WHITE, thickness=back_box_thickness+1)
        back_button.blit_box(BLACK, thickness=back_box_thickness)

        for i in range(len(input_text)):
            if input_text[i] != level_text[i]:
                wrong_indexes.add(i)



        results = events(level_text_box, back_button, level_active)

        if results != []:

            if results[0] in [True, False]:

                level_active = results[0]

            elif results[0] == 2:
                return [1] # BACK

            elif results[0] == 3:
                return [2] # QUIT

        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return [2] # QUIT

        if level_active:

            lst = [key for key in pressed_dict.keys()]

            for key in lst:
                if not pressed[ord(key)]:
                    del pressed_dict[key]

            for char in valid_characters:

                if keys[char] and char != 8 and not pressed[char]:
                    if keys[K_RSHIFT] or keys[K_LSHIFT]:
                        level_text_box.add_letter(UPPER_DICT[chr(char)], len(level_text))
                    else:
                        level_text_box.add_letter(chr(char), len(level_text))

                    if not start_time_check:
                        start_time = time.time()
                        start_time_check = True
                    
                    account.increment_total_keypresses()


                elif keys[char] and char == 8 and pressed[char]:
                    if timer(pressed_dict[chr(char)]):
                        level_text_box.remove_letter()

                        if len(input_text) == 0:
                            index = 0
                        else:
                            index = len(input_text)-1

                        letter=Letter(level_text[index],LIGHT_GREY,WHITE,screen,TEXT_FONT,TEXT_FONT_SIZE,[x_pos, y_pos])

                        letter.init_highlight()
                        letter.init_letter()
                        letter.blit_highlight()
                        letter.blit_letter()

                        letters.pop()


                elif keys[char] and char == 8 and not pressed[char]:
                    level_text_box.remove_letter()
                    pressed_dict[chr(char)] = time.time()

                    if len(input_text) == 0:
                            index = 0
                    else:
                        index = len(input_text)-1

                    letter=Letter(level_text[index],LIGHT_GREY,WHITE,screen,TEXT_FONT,TEXT_FONT_SIZE,[x_pos, y_pos])

                    letter.init_highlight()
                    letter.init_letter()
                    letter.blit_highlight()
                    letter.blit_letter()

                    letters.pop()

                    account.increment_total_keypresses()

        pressed = keys

        input_text = level_text_box.get_text()

        level_text_box_thickness = SELECTED_THICKNESS if level_active or level_text_box.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS
        back_box_thickness = SELECTED_THICKNESS if back_button.get_box().collidepoint(pygame.mouse.get_pos()) else DESELECTED_THICKNESS

        try:
            x_pos, y_pos = blitting_letters(runs, input_text, TEXT_FONT_SIZE, letters, level_text, wrong_indexes, screen, TEXT_FONT, DARK_COLOURS, LIGHT_COLOURS, TOP_BUFFER, SIDE_BUFFER)
        except TypeError:
            pass

        pygame.display.flip()

        if check:

            total = 0
            for i in range(len(input_text)):
                if input_text[i] == level_text[i]:
                    total += 1

            return [0, x, total*100//len(level_text)]

        if len(input_text) == len(level_text):
            check = True


if __name__ == '__main__':
    levels_screen(Account('tom','bed'))
    pygame.quit()
