# *********************** #
#   Author: Bruce Stull   #
#   Signature Generator   #
#       Version: 0.0      #
#        2022-01-04       #
# *********************** #

welcome_string = "\nWelcome to Signature Generator!\n"
print(welcome_string)

# TODO: Add functionality where I only get prompted for the project name and version number.
# Have other stuff pull from variables in this file or a separate file.

# Prompt user for "Author" name.
# author_name = input("Enter your name: ")
author_name = "Bruce Stull"

# Prompt user for 'Project Name'.
project_name = input("Please enter project name: ")

# Project sub-title.
project_subtitle = input("Please enter project subtitle: ")

# Prompt user for version number.
version_number = input("Please enter version number: ")

# Add blank line.
print()

# TODO: Add functionality where user decides whether to auto-populate current date or use manually entered date.
from datetime import date
current_date = date.today()
# # Prompt user for date.
# current_date = input("Please enter the date: ")

# Combine variables into a list so we can determine how wide to make the asterisk lines.
field_list = [project_name, project_subtitle, "Version: " + version_number, "Author: " + author_name, str(current_date)]
print(field_list)

field_sizes = []
for item in field_list:
    field_sizes.append(len(str(item)))
print(f"Field sizes: {field_sizes}")

# Create variable for how much padding to place on sides of longest character in signature_list.
padding = 2

pound_sign = '#'
asterisk = '*'

required_width = max(field_sizes) + padding*2
print(f"Required width: {required_width}")
# Add blank line.
print()

print(pound_sign, asterisk * required_width, pound_sign)
for item in field_list:
    print(pound_sign, item.center(required_width), pound_sign)
print(pound_sign, asterisk * required_width, pound_sign)
