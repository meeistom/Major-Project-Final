# Filename: digit_reboot_classes.py
# Author: Tom Bednarek
# Date: May, June 2021



import random
import time
from datetime import date
import os
import pygame
from digit_reboot_functions import *
from pygame.locals import *



STATISTICS_FILE = '_statistics_file.txt'
DETAILS_FILE = '_details_file.txt'



class Account:

    def __init__(self, username, password, level=0, total_keypresses=0, highest_WPM=0, average_WPM=0, last_10_average_WPM=0, join_date=date.today(), logged_wpms=0, last_10_wpms=[]):

        self.username = username
        self.password = password
        self.level = level
        self.total_keypresses = total_keypresses
        self.highest_WPM = highest_WPM                         
        self.average_WPM = average_WPM
        self.last_10_average_WPM = last_10_average_WPM
        self.join_date = join_date
        self.logged_wpms = logged_wpms
        self.last_10_wpms = last_10_wpms
        self.statistics_filename = username+STATISTICS_FILE
        self.details_filename = username+DETAILS_FILE

        self.save()

    def __str__(self):
        return f'{self.username}\n{self.password}\n{self.level}\n{self.total_keypresses}\n{self.highest_WPM}\n{self.statistics_filename}\n{self.details_filename}'

    def get_join_date(self):
        return self.join_date

    def get_username(self):
        return self.username
    
    def set_username(self, new_username, stats_file, details_file, accounts_file, delimiter):

        self.statistics_filename = new_username+stats_file
        self.details_filename = new_username+details_file

        self.save()
        os.remove(self.username+stats_file)
        os.remove(self.username+details_file)
        dct = file_to_dict(accounts_file, delimiter)           # THIS IS ACCOUNTS = 'accounts.txt'
        p = dct[self.username]
        del dct[self.username]
        dct[new_username] = p

        keys = [key for key in dct.keys()]
        insertion_sort(keys)                                           # INSERTION SORT HERE
        
        with open(accounts_file,'w', encoding='utf-8') as f:
            for key in keys:
                f.write(f'{key}{delimiter}{dct[key]}\n')

        self.username = new_username             

    def get_password(self):
        return self.password
    
    def set_password(self, new_password, accounts_file, delimiter):
        
        dct = file_to_dict(accounts_file, delimiter)           # THIS IS ACCOUNTS = 'accounts.txt'
        dct[self.username] = new_password
        
        keys = [key for key in dct.keys()]
        insertion_sort(keys)                                            # INSERTION SORT HERE
        
        with open(accounts_file,'w', encoding='utf-8') as f:
            for key in keys:
                f.write(f'{key}{delimiter}{dct[key]}\n')

        self.password = new_password

        self.save()
        
    def get_statistics_file(self):
        return self.statistics_filename
    
    def get_details_file(self):
        return self.details_filename

    def increment_level(self):
        self.level+=1

    def get_level(self):
        return self.level
    
    def set_level(self, new_level):
        self.level = new_level

    def increment_total_keypresses(self):
        self.total_keypresses+=1
    
    def get_total_keypresses(self):
        return self.total_keypresses
    
    def get_highest_WPM(self):
        return self.highest_WPM
    
    def set_highest_WPM(self, new_highest_WPM):
        self.highest_WPM = new_highest_WPM
    
    def set_last_10_average_WPM(self, new_wpm):
        if len(self.last_10_wpms) == 0:
            self.last_10_average_WPM = new_wpm
            self.last_10_wpms.append(new_wpm)
        else:
            total = 0
            if len(self.last_10_wpms) == 10:
                self.last_10_wpms.pop()
            self.last_10_wpms.insert(0, new_wpm)
            for wpm in self.last_10_wpms:
                total+=wpm
            self.last_10_average_WPM = round(total/len(self.last_10_wpms))

    def set_average_WPM(self, new_wpm):
        self.logged_wpms+=1
        self.average_WPM = round((self.average_WPM*(self.logged_wpms-1)+new_wpm)/(self.logged_wpms))
    
    def get_average_WPM(self):
        return self.average_WPM
    
    def get_last_10_average_WPM(self):
        return self.last_10_average_WPM

    def save(self):
        
        with open(self.statistics_filename,'w') as f:
            f.write(f'Total Kepresses:{self.total_keypresses}\nHighest WPM:{self.highest_WPM}\nAverage WPM:{self.average_WPM}\nLast 10 Average WPM:{self.last_10_average_WPM}\nLevel:{self.level}\nJoin Date:{self.join_date}')
        
        with open(self.details_filename,'w') as f:
            f.write(f'{self.username}\n{self.password}\n{self.level}\n{self.total_keypresses}\n{self.highest_WPM}\n{self.average_WPM}\n{self.last_10_average_WPM}\n{self.join_date}\n{self.logged_wpms}\n{" ".join([str(x) for x in self.last_10_wpms])}\n{self.statistics_filename}\n{self.details_filename}')



class Title:

    def __init__(self, text, font, font_size, screen, colour, screen_width):
        self.text = text
        self.font = font
        self.font_size = font_size
        self.screen = screen
        self.colour = colour
        self.screen_width = screen_width
    
    def blit(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        title_img = font.render(self.text, True, self.colour)
        self.screen.blit(title_img, [(self.screen_width-title_img.get_rect().width)/2, 100])



class Border:

    def __init__(self, lines, screen, colour):
        self.lines = lines
        self.screen = screen
        self.colour = colour
    
    def draw_border(self):
        for line in self.lines:
            pygame.draw.rect(self.screen, self.colour, line)



class Button:

    def __init__(self, width, height, text, thickness, colour, screen, font, font_size, box_position, text_position): # text = ''
        self.width = width
        self.height = height
        self.text = text
        self.box_position = box_position
        self.text_position = text_position
        self.thickness = thickness
        self.colour = colour
        self.screen = screen
        self.font = font
        self.font_size = font_size
    
    def init_box(self):
        self.box = Rect(self.box_position[0], self.box_position[1], self.width, self.height)
    
    def get_box(self):
        return self.box
    
    def get_text(self):
        return self.text
    
    def set_text(self, new_text):
        self.text = new_text
    
    def init_center_text(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.text_img = font.render(self.text, True, self.colour)
        self.text_rect = self.text_img.get_rect(center=self.text_position)
        
    def set_thickness(self, new_thickness):
        self.thickness = new_thickness

    def blit_box(self, box_colour, thickness=''):
        if thickness == '':
            pygame.draw.rect(self.screen, box_colour, self.box, self.thickness)
        elif thickness == None:
            pygame.draw.rect(self.screen, box_colour, self.box)
        else:
            pygame.draw.rect(self.screen, box_colour, self.box, thickness)
    
    def blit_center_text(self):
        self.screen.blit(self.text_img, self.text_rect)
    
    def blit_image(self, image):
        self.image = image
        self.image_rect = self.image.get_rect(center=self.text_position)
        self.screen.blit(self.image, self.image_rect)



class InputBox(Button):

    def __init__(self, width, height, text, thickness, colour, screen, font, font_size, box_position, text_position):

        Button.__init__(self, width, height, text, thickness, colour, screen, font, font_size, box_position, [0,0])
        self.text_position = text_position
    
    def init_side_text(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.text_img = font.render(self.text, True, self.colour)
    
    def init_flash(self, thickness):
        self.flash = Rect(self.text_position[0]+self.text_img.get_width(), self.text_position[1], thickness, self.font_size) # left, top, width, height
    
    def add_letter(self, letter, limit):
        if len(self.text) < limit:
            self.text += letter

    def remove_letter(self):
        self.text = self.text[:-1]

    def blit_side_text(self, censor, symbol=''):
        if censor:
            font = pygame.font.SysFont(self.font, self.font_size)
            self.text_img = font.render(len(self.text)*symbol, True, self.colour)


        self.screen.blit(self.text_img, self.text_position)

    def blit_watermark(self, watermark, colour):
        if self.text == '':
            font = pygame.font.SysFont(self.font, self.font_size)
            self.watermark_img = font.render(watermark, True, colour)
            self.screen.blit(self.watermark_img, self.text_position)

    def blit_permanent_watermark(self, watermark, colour, rect=[]):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.watermark_img = font.render(watermark, True, colour)

        if rect != []:
            self.screen.blit(self.watermark_img, self.text_position, area=rect)
        else:
            self.screen.blit(self.watermark_img, self.text_position)
    
    def blit_flash(self, on):
        if on:
            pygame.draw.rect(self.screen, self.colour, self.flash)



class Letter:

    def __init__(self, letter, letter_colour, highlight_colour, screen, font, font_size, position):
        self.width = round((font_size+3)*9/16)
        self.height = font_size+3
        self.letter = letter
        self.letter_colour = letter_colour
        self.highlight_colour = highlight_colour
        self.screen = screen
        self.font = font
        self.font_size = font_size
        self.position = position
        self.drawn = False

    def get_drawn(self):
        return self.drawn

    def set_drawn(self, bool):
        self.drawn = bool

    def init_highlight(self):
        self.highlight = Rect(self.position[0], self.position[1], self.width, self.height)

    def init_letter(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.letter_img = font.render(self.letter, True, self.letter_colour)
    
    def blit_highlight(self):
        pygame.draw.rect(self.screen, self.highlight_colour, self.highlight)
    
    def blit_letter(self):
        self.screen.blit(self.letter_img, self.position)

        

class Key:

    def __init__(self, width, height, letters, key_colour, background_colour, thickness, screen, radius, font, font_size, active, box_position, text_position=[], text_buffer=None):
        self.width = width
        self.height = height
        self.letters = letters
        self.key_colour = key_colour
        self.background_colour = background_colour
        self.thickness = thickness
        self.screen = screen
        self.radius = radius
        self.font = font 
        self.font_size = font_size
        self.active = active
        self.box_position = box_position
        self.text_position = text_position
        self.text_buffer = text_buffer

    def __str__(self):
        return self.letters[0]

    def set_active(self, value):
        self.active = value
    
    def get_active(self):
        return self.active

    def get_letters(self):
        return self.letters

    def get_width(self):
        return self.width

    def init_box(self):
        self.box = Rect(self.box_position[0], self.box_position[1], self.width, self.height)   

    def init_center_letter(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.letter_img = font.render(self.letters[0], True, self.key_colour)
        self.letter_rect = self.letter_img.get_rect(center=self.text_position)

    def init_side_text(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.side_text_img = font.render(self.letters[0], True, self.key_colour)

    def init_stacked_center_letters(self):
        font = pygame.font.SysFont(self.font, self.font_size)
        self.top_text_img = font.render(self.letters[1], True, self.key_colour)
        self.bottom_text_img = font.render(self.letters[0], True, self.key_colour)

        self.top_text_position = [self.text_position[0], self.text_position[1]-self.font_size/1.5]
        self.bottom_text_position = [self.text_position[0], self.text_position[1]+self.font_size/1.5]

        self.top_letter_rect = self.top_text_img.get_rect(center=self.top_text_position)
        self.bottom_letter_rect = self.bottom_text_img.get_rect(center=self.bottom_text_position)

    def blit_box(self):
        pygame.draw.rect(self.screen, self.background_colour, self.box, border_radius=self.radius)
        pygame.draw.rect(self.screen, self.key_colour, self.box, self.thickness, self.radius)

    def blit_center_letter(self):
        self.screen.blit(self.letter_img, self.letter_rect)
    
    def blit_left_side_text(self):
        self.screen.blit(self.side_text_img, self.text_position)

    def blit_right_side_text(self): # text_position [left, top]
        self.text_position[0] = self.text_position[0] + self.width - self.side_text_img.get_width() - self.text_buffer
        self.screen.blit(self.side_text_img, self.text_position)

    def blit_stacked_center_letters(self):
        self.screen.blit(self.top_text_img, self.top_letter_rect)
        self.screen.blit(self.bottom_text_img, self.bottom_letter_rect)

    def change_background_colour(self, new_background_colour):
        if self.active:
            self.background_colour = new_background_colour
        else:
            self.background_colour = new_background_colour
