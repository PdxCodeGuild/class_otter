# *********************** #
#         Copy Pad        #
#      2022 - 01 - 23     #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-23       #
# *********************** #

import lab14

the_joke_list = lab14.submit_search_request_get_json('hipster')

print(f"Type: {type(the_joke_list)}")
print(the_joke_list)