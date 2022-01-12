# Lab 3: Number to Phrase
# Convert a given number into its English text represetation.  Ex: 67 becomes 'sixty-seven'.

# Version 1
# Convert a given number into its English text represetation.  Ex: 67 becomes 'sixty-seven'.

# Version 2
# Update this to handle numbers 100-999
number = input('provide a number: ')
number = int(number)

hundred = number // 100
tens = number // 10
singles = number % 10

output = ''

single_digit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# special cases for ten, eleven, twelve, thirteen
tens_digit = ['teen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

if number == 0:
    output = 'zero'

if number >= 100:
    output = f'{single_digit[hundred - 1]} hundred '
    number = number % 100
    tens = number // 10

if tens == 0 and singles > 0:
    output += single_digit[singles - 1]
elif tens == 1 and singles == 0:
    output += 'ten'
elif tens == 1 and singles == 1:
    output += 'eleven'
elif tens == 1 and singles == 2:
    output += 'twelve'
elif tens == 1 and singles == 3:
    output += 'thirteen'
elif tens == 1:
    output += f'{single_digit[singles - 1]}teen'
elif tens >= 2 and tens < 10:
    if singles == 0:
        output += tens_digit[tens - 1]
    else:
        output += f'{tens_digit[tens - 1]}-{single_digit[singles - 1]}'


print(output)
# print(hundreds+output)
        

# do this in ranges?, - less than ten
# could maybe make a function with optional parameters? to make the above cleaner? or nest it above so it's not in the body of the code 
# could also be done with dictionaries


# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.