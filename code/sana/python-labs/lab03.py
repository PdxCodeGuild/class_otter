tens_converter = {
    6 : 'sixty',
    7 : 'seventy',
    8 : 'eighty',
    5 : 'fifty',
    4 : 'forty',
    3 : 'thirty',
    2 : 'twenty',
    9 : 'ninety',
    0 : '',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'forteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen'
}
ones_converter = {
    0 : 'zero',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine'
}
zo_converter = {
    0 : '',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine'
}
h_converter = {
    1 : 'one hundred',
    2 : 'two hundred',
    3 : 'three hundred',
    4 : 'four hundred',
    5 : 'five hundred',
    6 : 'six hundred',
    7 : 'seven hundred',
    8 : 'eight hundred',
    9 : 'nine hundred'
}
teen_converter ={
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'forteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen'
}
def t_digits(x):
    tens_digit = x//10
    # print(tens_digit)
    return tens_digit
def o_digits(y):
    ones_digit = y%10
    # print(ones_digit)
    return ones_digit
def th_digits(v):
    th_digit = (v //100)
    th_digit = th_digit * 100
    th_digit = (v - th_digit)
    # print(th_digit)
    if th_digit >= 10 and th_digit < 20:
        # print(th_digit)
        return th_digit
    elif th_digit >= 20 or th_digit < 10:
        th_digit = th_digit//10
    # print(th_digit)
    return th_digit
def h_digits(z):
    hundreds_digit = z //100
    # print(hundreds_digit)
    return hundreds_digit
while True:
    entered_number = input("enter your number or 'quit' to quit: ")
    if entered_number == 'quit':
        break
    entered_number = int(entered_number)
    if entered_number < 20 and entered_number > 10:
        print(teen_converter[entered_number])
    elif entered_number == 10:
        print('ten')
    elif entered_number < 10:
        ones = ones_converter[o_digits(entered_number)]
        print(ones)
    elif entered_number > 19 and entered_number < 100:
        tens = tens_converter[t_digits(entered_number)]
        ones = zo_converter[o_digits(entered_number)]
        print(f'{tens} {ones}')
    elif entered_number > 99:
        if th_digits(entered_number) == 1:
            teens = teen_converter[entered_number]
            hundreds = h_converter[h_digits(entered_number)]
            print(f'{hundreds} {teens}')
        elif th_digits(entered_number) != 1:
            tens = tens_converter[th_digits(entered_number)]
            hundreds = h_converter[h_digits(entered_number)]
            test = entered_number // 100
            test = entered_number - (test * 100)
            if test >= 20 or test < 10:
                ones = zo_converter[o_digits(entered_number)]
                print(f'{hundreds} {tens} {ones}')
            else:
                print(f'{hundreds} {tens}')