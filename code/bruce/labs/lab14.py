# ********************************** #
#        Lab 14: Dad Joke API        #
#   request http GET response json   #
#            Version: 1.0            #
#        Author: Bruce Stull         #
#             2022-01-22             #
# ********************************** #

import time

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/14%20Dad%20Joke%20API.md

# Lab 14: Dad Joke API

# Use the Dad Joke API to get a dad joke and display it to the user.
# You may want to also use time.sleep to add suspense.

# Part 1
    # Use the requests library to send an HTTP request to https://icanhazdadjoke.com/
    # with the accept header as application/json. This will return a dad joke in JSON format.
    # You can then use the .json() method on the response to get a dictionary.
    # Get the joke out of the dictionary and show it to the user.

# Part 2 (optional)
    # Add the ability to "search" for jokes using another endpoint.
    # Create a REPL that allows one to enter a search term and go through jokes one at a time.
    # You can also add support for multiple pages.