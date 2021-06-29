# File name: digit_reboot_functions.py
# Author: Tom Bednarek
# Date: May 2021



import time
import random
import pygame
from pygame.locals import *

#from digit_reboot_classes import Account



### CONSTANTS ###

AVERAGE_WORD_LENGTH = 4.84
RANGE = 10
ACCOUNTS = 'accounts.txt'
#DICTIONARY = 'dictionary.txt'              # make option to either do harder one or easier one
DICTIONARY = 'common_words.txt'             # make option to either do harder one or easier one
RESPONSE = 'Type it as quickly as you can!\n'
LEVELS = 'levels.txt'

###



def rainbow_colour():
    '''Creates an array of tuples which stores RGB light values.'''
    lst = [(255, 0, 0)]

    i = 255
    j = 0
    k = 0

    while True:
        if i == 255 and j != 255 and k == 0:
            j+=1
            lst.append((i,j,k))
        elif i <= 255 and j == 255 and k == 0 and i != 0:
            i-=1
            lst.append((i,j,k))
        elif i == 0 and j == 255 and k != 255:
            k+=1
            lst.append((i,j,k))
        elif i == 0 and j <= 255 and k == 255 and j != 0:
            j-=1
            lst.append((i,j,k))
        elif i != 255 and j == 0 and k == 255:
            i+=1
            lst.append((i,j,k))
        elif i == 255 and j == 0 and k <= 255 and k != 1:
            k-=1
            lst.append((i,j,k))
        else:
            break
            

    return lst



def on():
    '''Returns True for half a second and False for the other half.'''
    current_time = time.time()
    if current_time-int(current_time) > 0.5:
        return False
    else:
        return True



def fill_blanks(n, char):
    '''Adds a character to the start of a string while the length of the string is less than 3.'''
    while len(n) < 3:
        n = char+n
    return n



def insertion_sort(lst):
    '''Performs an Insertion Sort on a given array.'''
    num_items = len(lst)
    current_item = 1

    while current_item < num_items:
        current_data_item = lst[current_item]
        comparison = 0
        finish = False

        while comparison < current_item and finish == False:

            if current_data_item < lst[comparison]:
                shuffle_item = current_item

                while shuffle_item > comparison:
                    lst[shuffle_item] = lst[shuffle_item-1]
                    shuffle_item -= 1

                lst[comparison] = current_data_item
                finish = True

            comparison += 1

        current_item += 1



def login(accounts, username, password):
    '''Checks if the username input by the user matches with a password to be able to log into an account.'''
    if username in accounts.keys():
        if password == accounts[username]:
            return True
    return False



def register(usernames, username):  # THIS IS A LINEAR SEARCH FUNCTION THAT HAS BEEN NAMED 'register'
    '''Returns True or False based on whether a username is in a array or not.'''
    if username in usernames:
        return False
    return True



def create_account(username, password, delimiter, accounts):
    from digit_reboot_classes import Account
    '''Creates an account.'''
    dct = file_to_dict(accounts, delimiter)
    dct[username] = password

    keys = [key for key in dct.keys()]
    insertion_sort(keys)                                           # need to write your own sort

    with open(accounts,'w', encoding='utf-8') as f:
        for key in keys:
            f.write(f'{key}{delimiter}{dct[key]}\n')

    return Account(username, password)



def open_account(username, details_file):
    from digit_reboot_classes import Account
    '''Loads the users account details into the program.'''
    details = file_to_lst(username+details_file)
    return Account(details[0], details[1], int(details[2]), int(details[3]), int(details[4]), int(details[5]), int(details[6]), details[7], int(details[8]), [int(x) for x in details[9].split()])



def file_to_lst(filename):
    '''Converts a file to a list.'''
    try:
        with open(filename,'r', encoding='utf-8') as f:
            lst = f.readlines()
    except FileNotFoundError:
        with open(filename,'a', encoding='utf-8') as f:
            return []

    return [element.strip('\n') for element in lst] # put '\n' in strip, hopefully doesn't break anything



def file_to_dict(filename, delimiter):
    '''Converts a file to a dictionary.'''
    lst = file_to_lst(filename)
    return {row.split(delimiter)[0]: row.split(delimiter)[1] for row in lst}



def WPM_gen():
    '''Generates a random text.'''
    lst = file_to_lst(DICTIONARY)
    text = ''
    for i in range(RANGE):
        text+= lst[random.randint(0,len(lst)-1)] +' '
    text = text.lower().strip()
    return text



def test():
    '''Times how long it takes to complete a test.'''
    start_time = time.time()
    response = input(RESPONSE).strip()
    end_time = time.time()

    elapsed_scaled = 60/(end_time-start_time)

    return response, elapsed_scaled



def WPM_comparer(WPM1, WPM2):
    '''Compares to see which WPM is higher.'''
    if WPM1 > WPM2:
        return WPM1
    else:
        return WPM2



def WPM_calculator(text, response, time_factor):
    '''Calculates what the WPM was for a certain text.'''
    n=0
    for i in range(0,len(response)):
        if text[i] == response[i]:
            n+=1

    return round(n*time_factor//AVERAGE_WORD_LENGTH) # removed int(n*time_factor) but may want to put it back at some point



def level(user):
    '''Retreives the text for the user's level.'''
    levels = file_to_lst(LEVELS)
    return levels[int(user.get_level())]



def timer(start_time):
    '''Returns True for half a second and False for the other half.'''
    if time.time()-start_time > 0.5:
        return True
    else:
        return False



def limit_sentences(text, run_length):
    '''Make sure runs don't finish in the middle of a word but at a space.'''
    runs = []

    start=0
    end=run_length
    check=False

    while True:

        try:
            while text[end-1] != ' ':
                end-=1
        except IndexError:
            pass

        runs.append(text[start:end])
        start = end
        end += run_length

        if check:
            break
        if end > len(text):
            check = True
    
    return runs



def temp_WPM_calculator(start_time, chars, average_word_length):
    elapsed_time = 60/(time.time()-start_time)
    return round(chars*elapsed_time//average_word_length)



def beginning_blit(screen_width, screen_height, screen, white, black, light_grey, back_box_width, input_box_width, input_box_height, back, back_box_thickness, text_font, text_font_size, WPM_text, WPM_text_box_thickness, WPM_test_box_thickness, WPM_test_box_width, wpm_test_text, top_buffer, side_buffer):
    screen.fill(white)
    
    from digit_reboot_classes import Button, InputBox, Border
    import pygame

    top_line = pygame.Rect(0, 0, screen_width, 2) # left, top, width, height
    right_line = pygame.Rect(screen_width-2, 0, 2, screen_height) # left, top, width, height
    bottom_line = pygame.Rect(0, screen_height-2, screen_width, 2) # left, top, width, height
    left_line = pygame.Rect(0, 0, 2, screen_height) # left, top, width, height
    lines=[top_line, right_line, bottom_line, left_line]

    border = Border(lines, screen, black)
    border.draw_border()

    back_button = Button(
            back_box_width, 
            input_box_height,
            back,
            back_box_thickness,
            black,
            screen,
            text_font,
            text_font_size,
            [screen_width-back_box_width-side_buffer, screen_height-input_box_height-top_buffer],
            [screen_width-back_box_width/2-side_buffer, (screen_height-input_box_height-top_buffer+text_font_size*1.5)]
        )

    back_button.init_center_text()
    back_button.blit_center_text()

    run_length = round((input_box_width-text_font_size*2)/int(text_font_size*9/16+1))+1 # THIS ACCOUNTS FOR THE SPACE >>> the +1
    # SOMEHOW THAT COMMENT ABOVE MAKES SENSE TO ME NOW

    runs = limit_sentences(WPM_text, run_length)
    
    run_boxes = []
    n=1
    for run in runs:

        run_boxes.append(InputBox(
            input_box_width,
            input_box_height,
            '',
            WPM_text_box_thickness,
            black,
            screen,
            text_font,
            text_font_size,
            [side_buffer,top_buffer],
            [side_buffer+text_font_size,top_buffer+text_font_size*n*2]
        ))
        n+=1

    n=0
    for run in run_boxes:

        run.blit_permanent_watermark(runs[n], light_grey)
        n+=1
    
    WPM_test_box = Button(
        WPM_test_box_width,
        input_box_height,
        wpm_test_text,
        WPM_test_box_thickness,
        black,
        screen,
        text_font,
        text_font_size,
        [screen_width/2-WPM_test_box_width/2, screen_height-input_box_height-top_buffer],
        [screen_width/2, screen_height-input_box_height/2-top_buffer]
    )

    WPM_test_box.init_box()
    WPM_test_box.init_center_text()
    WPM_test_box.blit_box(black)
    WPM_test_box.blit_center_text()

    return back_button, runs



def blitting_letters(runs, input_text, font_size, letters, example_text, wrong_indexes, screen, font, dark_colours, light_colours, side_buffer, top_buffer):
    
    from digit_reboot_classes import Letter
    
    i = len(input_text)-1

    if i == -1:
        return

    total_letters = 0
    for x in range(len(runs)):
        previous_total_letters = total_letters
        total_letters += len(runs[x])
        if i < total_letters:
            break
    
    n = i-previous_total_letters

    x_pos = side_buffer+font_size+n*int(font_size*9/16+1)
    y_pos = top_buffer+font_size*2*(x+1)

    if input_text[i] == example_text[i] and i in wrong_indexes:

        letters.append(Letter(
            example_text[i],
            dark_colours[1],
            light_colours[1],
            screen,
            font,
            font_size,
            [x_pos, y_pos]
        ))
        n+=1

    elif i in wrong_indexes:
        letters.append(Letter(
            example_text[i],
            dark_colours[2],
            light_colours[2],
            screen,
            font,
            font_size,
            [x_pos, y_pos]
        ))
        n+=1

    else:
        letters.append(Letter(
            example_text[i],
            dark_colours[0],
            light_colours[0],
            screen,
            font,
            font_size,
            [x_pos, y_pos]
        ))
        n+=1

    for letter in letters:
        if not letter.get_drawn():
            letter.init_highlight()
            letter.init_letter()
            letter.blit_highlight()
            letter.blit_letter()
            letter.set_drawn(True)

    return x_pos, y_pos



def events(text_box, button, active):
    result = []
    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:

            if text_box.get_box().collidepoint(event.pos):
                result.append(not active)
            
            elif button.get_box().collidepoint(event.pos):
                result.insert(0, 2)
            
            else:
                result.append(False)
        
        elif event.type == QUIT:
            result.insert(0, 3)
    
    return result



def create_keyboard(keyboard_font, arrow_font, font_size, key_thickness, keyboard_thickness, black, light_grey, light_blue, white, key_width, key_height, key_spacing, 
    radius, number_row_keys, top_row_keys, home_row_keys, bottom_row_keys, function_row_keys, screen, text_buffer, top_left_corner, active_lst):
    from digit_reboot_classes import Key

    keys=[]

    back_quote_factor = -key_width/2

    back_quote = Key(key_width+back_quote_factor, key_height, number_row_keys[0], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+text_buffer,top_left_corner[1]+text_buffer], [top_left_corner[0]+(key_width+back_quote_factor)/2+text_buffer,top_left_corner[1]+key_height/2+text_buffer])

    keys.append(back_quote)

    for i in range(1,len(number_row_keys)-1):
        keys.append(Key(key_width, key_height, number_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+back_quote_factor+text_buffer,top_left_corner[1]+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*i+back_quote_factor+text_buffer,top_left_corner[1]+key_height/2+text_buffer]))

    i+=1

    backspace_factor = key_width*9/10

    backspace = Key(key_width+backspace_factor, key_height, number_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+back_quote_factor+text_buffer,top_left_corner[1]+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*i+back_quote_factor+text_buffer,top_left_corner[1]+key_height/2-font_size/2+text_buffer], text_buffer)

    keys.append(backspace)






    background_width = 0
    for key in keys:
        background_width += key.get_width()
        background_width += key_spacing

    background_width += text_buffer*2-key_spacing
    background_height = key_height*5+key_spacing*4+text_buffer*2

    background = Key(background_width, background_height, '', black, light_grey, keyboard_thickness, screen, int(radius*1.5), keyboard_font, font_size, False, top_left_corner)

    keys.insert(0, background)





    tab_factor = key_width*1/5

    tab = Key(key_width+tab_factor, key_height, top_row_keys[0], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+text_buffer,top_left_corner[1]+key_height+key_spacing+text_buffer], [top_left_corner[0]+text_buffer*2,top_left_corner[1]+key_height*1.5+key_spacing-font_size/2+text_buffer])

    keys.append(tab)

    for i in range(1,len(top_row_keys)-1):
        keys.append(Key(key_width, key_height, top_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+tab_factor+text_buffer,top_left_corner[1]+key_height+key_spacing+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*i+tab_factor+text_buffer,top_left_corner[1]+key_height*1.5+key_spacing+text_buffer]))

    i+=1

    backslash_factor = key_width*1/5

    backslash = Key(key_width+backslash_factor, key_height, top_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+tab_factor+text_buffer,top_left_corner[1]+key_height+key_spacing+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*i+tab_factor*1.5+text_buffer,top_left_corner[1]+key_height*1.5+key_spacing+text_buffer])
    
    keys.append(backslash)




    caps_lock_factor = key_width*2/5

    caps_lock = Key(key_width+caps_lock_factor, key_height, home_row_keys[0], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+text_buffer,top_left_corner[1]+key_height*2+key_spacing*2+text_buffer], [top_left_corner[0]+text_buffer*2,top_left_corner[1]+key_height*2.5+key_spacing*2-font_size/2+text_buffer])

    keys.append(caps_lock)

    for i in range(1, len(home_row_keys)-1):
        keys.append(Key(key_width, key_height, home_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+caps_lock_factor+text_buffer,top_left_corner[1]+key_height*2+key_spacing*2+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*i+caps_lock_factor+text_buffer,top_left_corner[1]+key_height*2.5+key_spacing*3-font_size/2+text_buffer]))

    i+=1

    enter_factor = key_width*11/10

    enter = Key(key_width+enter_factor, key_height, home_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+caps_lock_factor+text_buffer,top_left_corner[1]+key_height*2+key_spacing*2+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*i+caps_lock_factor+text_buffer,top_left_corner[1]+key_height*2.5+key_spacing*3-font_size/2+text_buffer-font_size/2], text_buffer)
    
    keys.append(enter)





    l_shift_factor = key_width

    l_shift = Key(key_width+l_shift_factor, key_height, bottom_row_keys[0], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+text_buffer,top_left_corner[1]+key_height*3+key_spacing*3+text_buffer], [top_left_corner[0]+text_buffer*2,top_left_corner[1]+key_height*3+key_spacing*3+key_height/2-font_size/2+text_buffer])

    keys.append(l_shift)

    for i in range(1, len(bottom_row_keys)-1):
        keys.append(Key(key_width, key_height, bottom_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+l_shift_factor+text_buffer,top_left_corner[1]+key_height*3+key_spacing*3+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*i+l_shift_factor+text_buffer,top_left_corner[1]+key_height*3+key_spacing*4+key_height/2-font_size/2+text_buffer]))

    i+=1

    r_shift_factor = key_width*(1+3/5)

    r_shift = Key(key_width+r_shift_factor, key_height, bottom_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+l_shift_factor+text_buffer,top_left_corner[1]+key_height*3+key_spacing*3+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*i+l_shift_factor+text_buffer,top_left_corner[1]+key_height*3+key_spacing*4+key_height/2-font_size/2+text_buffer-font_size/2], text_buffer)
    
    keys.append(r_shift)





    l_ctrl_factor = -key_width*1/10

    l_ctrl = Key(key_width+l_ctrl_factor, key_height, function_row_keys[0], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+text_buffer], [top_left_corner[0]+text_buffer*2,top_left_corner[1]+key_height*4.5+key_spacing*4+text_buffer-font_size/2])

    keys.append(l_ctrl)

    for i in range(1,4):
        keys.append(Key(key_width, key_height, function_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*i+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4.5+key_spacing*4+text_buffer]))

    i+=1

    space_factor = key_width*(4+2/5)

    space = Key(key_width+space_factor, key_height, function_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+text_buffer])

    keys.append(space)

    for i in range(5,7):
        keys.append(Key(key_width, key_height, function_row_keys[i], black, white, key_thickness, screen, radius, keyboard_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+space_factor+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+text_buffer], [top_left_corner[0]+key_width/2+(key_width+key_spacing)*(i+4)+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4.5+key_spacing*4+text_buffer])) # plus 4 because spacebar takes up an extra 4 keys

    i+=1

    minus_part = 0
    for key in keys[-7:]:
        minus_part += key.get_width()
        minus_part += key_spacing

    arrow_factor = (background_width-text_buffer*2-minus_part-key_spacing*2)/3-key_width

    left_arrow = Key(key_width+arrow_factor, (key_height-key_spacing)/2, function_row_keys[i], black, white, key_thickness, screen, radius, arrow_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+space_factor+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+(key_height+key_spacing)/2+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*(i+4)+l_ctrl_factor+(key_width+arrow_factor)/2+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+(key_height-key_spacing)*3/4+key_spacing+text_buffer])

    keys.append(left_arrow)

    i+=1

    up_arrow = Key(key_width+arrow_factor, (key_height-key_spacing)/2, function_row_keys[i], black, white, key_thickness, screen, radius, arrow_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*i+space_factor+arrow_factor+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*(i+4)+arrow_factor+l_ctrl_factor+text_buffer+(key_width+arrow_factor)/2,top_left_corner[1]+key_height*4+key_spacing*4+(key_height-key_spacing)*1/4+text_buffer])

    keys.append(up_arrow)

    i+=1 # but for down arrow i+3 instead of i+4

    down_arrow = Key(key_width+arrow_factor, (key_height-key_spacing)/2, function_row_keys[i], black, white, key_thickness, screen, radius, arrow_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*(i-1)+space_factor+arrow_factor+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+(key_height+key_spacing)/2+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*(i+3)+arrow_factor+l_ctrl_factor+(key_width+arrow_factor)/2+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+(key_height-key_spacing)*3/4+key_spacing+text_buffer])

    keys.append(down_arrow)

    i+=1

    right_arrow = Key(key_width+arrow_factor, (key_height-key_spacing)/2, function_row_keys[i], black, white, key_thickness, screen, radius, arrow_font, font_size, False, [top_left_corner[0]+(key_width+key_spacing)*(i-1)+space_factor+arrow_factor*2+l_ctrl_factor+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+(key_height+key_spacing)/2+text_buffer], [top_left_corner[0]+(key_width+key_spacing)*(i+3)+arrow_factor+l_ctrl_factor+(key_width+arrow_factor)/2+text_buffer,top_left_corner[1]+key_height*4+key_spacing*4+(key_height-key_spacing)*3/4+key_spacing+text_buffer])

    keys.append(right_arrow)


    for i in range(1, len(keys)-1):
        if active_lst[i] == True:
            keys[i].set_active(True)
            keys[i].change_background_colour(light_blue)
        else:
            keys[i].set_active(False)
            keys[i].change_background_colour(white)
    

    for key in keys:
        if key in [tab, caps_lock, l_shift, l_ctrl]: # need to fix backspace, enter and r_shift to be right side justified, triangles for arrows
            key.init_box()
            key.init_side_text()
            key.blit_box()
            key.blit_left_side_text()
        elif key in [backspace, enter, r_shift]:
            key.init_box()
            key.init_side_text()
            key.blit_box()
            key.blit_right_side_text()
        elif key in [space, background]:
            key.init_box()
            key.blit_box()
        elif len(key.get_letters()) == 1 or key.get_letters()[0] in number_row_keys:
            key.init_box()
            key.init_center_letter()
            key.blit_box()
            key.blit_center_letter()
        else:
            key.init_box()
            key.init_stacked_center_letters()
            key.blit_box()
            key.blit_stacked_center_letters()
    
    new_active_lst = []
    for key in keys:
        if key.get_active():
            new_active_lst.append(True)
        else:
            new_active_lst.append(False)

    return keys, background_width, background_height, new_active_lst
