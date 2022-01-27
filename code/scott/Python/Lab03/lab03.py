'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*         Lab 03 - Number to Phrase         *
*             05/January/2022               *
*                                           *
*********************************************
'''
ones_digits = {1: "one", 
    2: "two", 
    3: "three", 
    4: "four", 
    5: "five", 
    6: "six", 
    7: "seven", 
    8: "eight", 
    9: "nine", 
    0: "zero"}
teen_digits = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "ninteen"
}
tens_digits = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
    10: "one hundred",
    20: "two hundred",
    30: "three hundred",
    40: "four hundred",
    50: "five hundred",
    60: "six hundred",
    70: "seven hundred",
    80: "eight hundred",
    90: "nine hundred",
}


num = []
num = int(input("please enter a number between 0 and 999:"))
num_div_ten = num // 10
num_remainder = num % 10
num_div_hundred = num // 100

if num_div_ten == 0: # single digits
    string_num = ones_digits.get(num)
    print (string_num)
elif num_div_ten == 1: # teens digits
    string_num = teen_digits.get(num)
    print (string_num)
elif num_div_ten > 1 and num_div_ten < 11 and num_remainder > 0: # numbers 20 through 109
    tens_string_num = tens_digits.get(num_div_ten)
    ones_string_num = ones_digits.get(num_remainder)
    string_num = str(tens_string_num) + "-" + str(ones_string_num)
    #string_num = "{}-{}".format(str(tens_string_num), str(ones_string_num))
    print(string_num)
elif num_div_ten > 1 and num_div_ten < 11 and num_remainder < 1: # numbers 20 through 109
    tens_string_num = tens_digits.get(num_div_ten)
    ones_string_num = ones_digits.get(num_remainder)
    string_num = str(tens_string_num)
    #string_num = "{}-{}".format(str(tens_string_num), str(ones_string_num))
    print(string_num)    
elif num_div_ten%10 == 1 and num > 100: # teen numbers over 100
    teen_num = num - (num_div_ten - 1) * 10
    teen_string_num = teen_digits.get(teen_num)
    hundred_num = num_div_ten - 1
    hundred_string_num = tens_digits.get(hundred_num)
    string_num = str(hundred_string_num) + " " + (teen_string_num)
    print(string_num)
elif num%100 == 0: #numbers divisible by 100
    hundred_num = (num // 100) * 10 
    string_num = tens_digits.get(hundred_num)
    print(string_num)
elif num_div_ten > 11 and num_div_ten < 100 and num_div_ten%10 > 1 and num_div_ten%10 < 10 and num%100 != 0 and num_remainder == 0: #numbers over 100 excluding teens
    hundred_num = (num // 100) * 10 
    hundred_string_num = tens_digits.get(hundred_num)
    tens_num = num_div_ten%10
    tens_string_num = tens_digits.get(tens_num)
    string_num = str(hundred_string_num) + " " +(tens_string_num)
    print(string_num)
elif num_div_ten > 11 and num_div_ten < 100 and num_div_ten%10 != 1 and num%100 != 0 and num_remainder > 0 : #numbers over 100 excluding teens
    hundred_num = (num // 100) * 10 
    hundred_string_num = tens_digits.get(hundred_num)
    tens_num = num_div_ten%10
    tens_string_num = tens_digits.get(tens_num)
    ones_string_num = ones_digits.get(num_remainder)
    string_num = str(hundred_string_num) + " " +(tens_string_num) + "-" + (ones_string_num)
    print(string_num)
else:
     print("This is an unacceptable number.")