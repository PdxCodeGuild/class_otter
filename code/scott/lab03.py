first_ten_digits = {1: "one", 
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
    10: "one hundred"
}

num = []
num = int(input(" please"))

tens_place = num // 10
ones_place = num % 10

if tens_place == 0:
    string_num = first_ten_digits.get(num)
    print (string_num)
elif tens_place == 1:
    string_num = teen_digits.get(num)
    print (string_num)
elif tens_place > 1 and tens_place < 11:
    tens_string_num = tens_digits.get(tens_place)
    ones_string_num = first_ten_digits.get(ones_place)
    string_num = str(tens_string_num) + "-" + str(ones_string_num)
    #string_num = "{}-{}".format(str(tens_string_num), str(ones_string_num))
    print(string_num)
elif tens_place%10 == 1:
    teen_num = num - (tens_place - 1)*10
    teen_string_num = teen_digits.get(teen_num)
#    string_num = "one hundred " + str(teen_string_num)
#    print(string_num)
# elif tens_place > 11 and tens_place < 100 and tens_place%10 != 1:
#     pass
# else:
#     print("This is an unacceptable number.")