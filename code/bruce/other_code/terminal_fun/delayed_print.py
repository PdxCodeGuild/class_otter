# ***************************** #
#         Delayed Print         #
#   Uses: 'random' and 'time'   #
#          Version: 1.0         #
#      Author: Bruce Stull      #
#           2022-01-06          #
# ***************************** #

import random
import time
print('Rolling dice...')
time.sleep(3)
print('You rolled a', random.randint(1,6))