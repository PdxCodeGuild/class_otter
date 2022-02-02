# *********************** #
#        Slow Print       #
#       Uses: 'time'      #
#       Version: 1.0      #
#   Author: Bruce Stull   #
#        2022-01-06       #
# *********************** #

import time
message = 'hello world!'
for char in message:
  print(char, end='', flush=True)
  time.sleep(.2)
    