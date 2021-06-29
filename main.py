# Filename: main.py
# Author: Tom Bednarek
# Date: June 2021

from levels_instructions_screen import levels_instructions_screen
from login_screen import *
from register_screen import *
from main_menu_screen import *
from levels_screen import *
from wpm_test_screen import *
from statistics_screen import *
from settings_screen import *
from level_WPM_end_screen import *
from levels_instructions_screen import *

if __name__ == '__main__':

    ### CONSTANTS ###

    ACCOUNTS = 'accounts.txt'
    DETAILS_FILE = '_details_file.txt'
    DELIMITER = '≡' # chr(8801)


    ### VARIABLES ###

    register_check = True
    login_check = False
    main_menu_check = False
    levels_check = False
    wpm_test_check = False
    statistics_check = False
    settings_check = False
    level_WPM_end_check = False
    levels_instructions_check = False


    ### LOGIC ###

    while True:
        if register_check:
            register_check = False
            results = register_screen()

            if results[0] == 0:
                user = create_account(results[1], results[2], DELIMITER, ACCOUNTS)
                main_menu_check = True

            elif results[0] == 1:
                login_check = True
            
            elif results[0] == 2:
                pygame.quit()
                break

        elif login_check:
            login_check = False
            results = login_screen()

            if results[0] == 0:
                user = open_account(results[1], DETAILS_FILE)
                main_menu_check = True

            elif results[0] == 1:
                register_check = True
        
            elif results[0] == 2:
                pygame.quit()
                break


        elif main_menu_check:
            main_menu_check = False
            result = main_menu_screen()

            if result == 0:
                levels_instructions_check = True

            elif result == 1:
                wpm_test_check = True

            elif result == 2:
                statistics_check = True
            
            elif result == 3:
                login_check = True
            
            elif result == 4:
                settings_check = True
            
            elif result == 5:
                pygame.quit()
                break
            

        elif levels_instructions_check:
            levels_instructions_check = False
            if user.get_level() == 0:
                result = levels_instructions_screen()

                if result == 0:
                    levels_check = True
                
                elif result == 1:
                    main_menu_check = True
                
                elif result == 2:
                    user.save()
                    pygame.quit()
                    quit()
            else:
                levels_check = True


        elif levels_check:
            levels_check = False
            results = levels_screen(user)

            if results[0] == 0:
                wpm = results[1]
                accuracy = results[2]
                screen_number = 0
                level_WPM_end_check = True
                user.increment_level()
                user.save()

            elif results[0] == 1:
                main_menu_check = True

            elif results[0] == 2:
                user.save()
                pygame.quit()
                break

        elif wpm_test_check:
            wpm_test_check = False
            results = wpm_test_screen(user)

            if results[0] == 0:
                wpm = results[1]
                accuracy = results[2]
                screen_number = 1
                level_WPM_end_check = True

            elif results[0] == 1:
                main_menu_check = True

            elif results[0] == 2:
                user.save()
                pygame.quit()
                break


        elif statistics_check:
            statistics_check = False
            result = statistics_screen(user)

            if result == 0:
                main_menu_check = True
            
            elif result == 1:
                pygame.quit()
                break

        elif settings_check:
            settings_check = False
            result = settings_screen(user)
            if result == 0:
                main_menu_check = True
            elif result == 1:
                user.save()
                pygame.quit()
                break
        

        elif level_WPM_end_check:
            level_WPM_end_check = False
            result = level_WPM_end_screen(screen_number, user, wpm, accuracy)
            
            if result == 0 and screen_number == 0:
                levels_check = True
            
            elif result == 0 and screen_number == 1:
                wpm_test_check = True

            if result == 1:
                main_menu_check = True
            
            elif result == 2:
                user.set_average_WPM(wpm)
                user.set_last_10_average_WPM(wpm)
                user.set_highest_WPM(WPM_comparer(wpm, user.get_highest_WPM()))
                user.save()
                pygame.quit()
                break
            
            user.set_average_WPM(wpm)
            user.set_last_10_average_WPM(wpm)
            user.set_highest_WPM(WPM_comparer(wpm, user.get_highest_WPM()))
            user.save()
        
        try:
            user.save()
        except NameError:
            pass
