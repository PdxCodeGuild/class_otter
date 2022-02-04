ones_dict = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}

teens_dict = {
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}

tens_dict = {
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eightty",
    90 : "ninety"
}

hunds_dict = {
    100 : "one-hundred",
    200 : "two-hundred",
    300 : "three-hundred",
    400 : "four-hundred",
    500 : "five-hundred",
    600 : "six-hundred",
    700 : "seven-hundred",
    800 : "eight-hundred",
    900 : "nine-hundred"
}

number = input("0-999, choose a number: ")
number = int(number)
 
tens_digit1 = (number // 10) % 10
tens_digit2 = tens_digit1 * 10
ones_digit = number % 10
hunds_digit1 = number // 100
hunds_digit2 = hunds_digit1 * 100
teens_digit = number % 100 
# print(teens_digit)
# print(tens_digit1)
# print(tens_digit2)
# print(hunds_digit1)

if number < 100:
    if number in ones_dict:
        print(ones_dict[number])
    elif number in teens_dict:
        print(teens_dict[number])
    elif number in tens_dict:
        print(tens_dict[number])
    elif tens_digit2 in tens_dict and ones_digit in ones_dict:
        print(f"{tens_dict[tens_digit2]}-{ones_dict[ones_digit]}")
else:
    if number in hunds_dict: #if tens_digit == 0 and ones_digit == 0
        print(hunds_dict[number])
    elif tens_digit1 == 0:
        print(f"{hunds_dict[hunds_digit2]}-{ones_dict[ones_digit]}")
    elif tens_digit1 == 1:
        print(f"{hunds_dict[hunds_digit2]}-{teens_dict[teens_digit]}") 
    elif ones_digit == 0:   
        print(f"{hunds_dict[hunds_digit2]}-{tens_dict[tens_digit2]}")            
    elif hunds_digit2 in hunds_dict and tens_digit2 in tens_dict and ones_digit in ones_dict:
        print(f"{hunds_dict[hunds_digit2]}-{tens_dict[tens_digit2]}-{ones_dict[ones_digit]}")


        