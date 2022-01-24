# ********************************* #
#     Time Lapse Scanner Display    #
#   time sleep \b flush range len   #
#            Version: 1.0           #
#        Author: Bruce Stull        #
#             2022-01-20            #
# ********************************* #

import time

def console_display_scanner(time_delay = .007, number_of_cycles = 3, scanner_width = 45):
    '''Accepts arguments of time_delay, number_of_cycles, and scanner_width. Moves the console cursor back and forth at time_delay and length scanner_width.'''
    cycle = 1
    while cycle <= number_of_cycles:

        # Draw the spaces.
        for _ in range(scanner_width):
            print(' ', end='', flush=True)
            time.sleep(time_delay)

        # Draw the backspaces.
        for _ in range(scanner_width):
            print('\b', end='', flush=True)
            time.sleep(time_delay)
        
        cycle += 1

def main():

    console_display_scanner(.003,1,80)
    console_display_scanner(.003,1,40)
    console_display_scanner(.003,1,20)
    console_display_scanner(.003,1,10)
    console_display_scanner(.003,1,5)
    console_display_scanner(.003,1,2)

    # for width in range(50,1,-1):
    #     console_display_scanner(.003,1,width)

    # cycle = 1
    # number_of_cycles = 3
    
    # while cycle <= number_of_cycles:

    #     scanner_width = 45
    #     # scanner_field = ' ' * scanner_width
    #     time_delay = .007

    #     # Draw the spaces.
    #     for _ in range(scanner_width):
    #         print(' ', end='', flush=True)
    #         time.sleep(time_delay)

    #     # Draw the backspaces.
    #     for _ in range(scanner_width):
    #         print('\b', end='', flush=True)
    #         time.sleep(time_delay)
        
    #     cycle += 1

main()