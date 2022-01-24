# ********************************* #
#     Time Lapse Scanner Display    #
#   time sleep \b flush range len   #
#            Version: 1.0           #
#        Author: Bruce Stull        #
#             2022-01-20            #
# ********************************* #

import time

def console_display_scanner(
        scanner_width = 45,
        number_of_cycles = 3,
        time_delay = .007
        ):
    '''Accepts arguments of scanner_width, number_of_cycles,
    and time_delay. Moves the console cursor back and
    forth at time_delay and length scanner_width.
    '''
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

    console_display_scanner(80, 1, .003)
    console_display_scanner(40, 1, .003)
    console_display_scanner(20, 1, .003)
    console_display_scanner(10, 1, .003)
    console_display_scanner(5, 1, .003)
    console_display_scanner(2, 1, .003)
    
    print_string = "A string to obtain a length."
    print(print_string)
    console_display_scanner(len(print_string), 2, .003)

main()