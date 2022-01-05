# numbers = {
#     0 : "zero",
#     1 : "one",
#     2 : "two",
#     3 : "three",
#     4 : "four",
#     5 : "five",
#     6 : "six",
#     7 : "seven",
#     8 : "eight",
#     9 : "nine",
#     10 : "ten",
#     11 : "eleven",
#     12 : "twelve",
#     13 : "thirteen",
#     14 : "fourteen",
#     15 : "fifteen",
#     16 : "sixteen",
#     17 : "seventeen",
#     18 : "eighteen",
#     19 : "nineteen",
#     20 : "twenty",
#     30 : "thirty",
#     40 : "forty",
#     50 : "fifty",
#     60 : "sixty",
#     70 : "seventy",
#     80 : "eightty",
#     90 : "ninety"
# }

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

number = input("0-99, choose a number: ")
number = int(number)
 
tens_digit = number // 10
tens_digit = tens_digit * 10
ones_digit = number % 10

if number in ones_dict:
    print(ones_dict[number])
elif number in teens_dict:
    print(teens_dict[number])
elif number in tens_dict:
    print(tens_dict[number])
elif tens_digit in tens_dict and ones_digit in ones_dict:
    print(f"{tens_dict[tens_digit]}-{ones_dict[ones_digit]}")



# for key in numbers:
#     if key == tens_digit:
#         digit1 = numbers[key]
#         print(digit1)
#     elif key == ones_digit:
#         digit2 = numbers[key]
#         print(digit2)
# answer = print(f"{digit1}-{digit2}")






        