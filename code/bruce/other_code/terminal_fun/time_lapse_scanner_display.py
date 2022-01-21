# ********************************* #
#     Time Lapse Scanner Display    #
#   time sleep \b flush range len   #
#            Version: 1.0           #
#        Author: Bruce Stull        #
#             2022-01-20            #
# ********************************* #

import time

def main():

    cycle = 1
    number_of_cycles = 3
    
    while cycle <= number_of_cycles:

        scanner_width = 45
        # scanner_field = ' ' * scanner_width
        time_delay = .007

        # Draw the spaces.
        for _ in range(scanner_width):
            print(' ', end='', flush=True)
            time.sleep(time_delay)

        # Draw the backspaces.
        for _ in range(scanner_width):
            print('\b', end='', flush=True)
            time.sleep(time_delay)
        
        cycle += 1

main()