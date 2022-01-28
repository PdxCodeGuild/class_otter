ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine"}

teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
         17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens = {2: "twenty", 3: "thirty", 4: "fourty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety",
        }


user = int(input("please enter a number: "))
# 0-9
if user < 10:
    print(ones[user])
# 10-19
if user >= 10 and user <= 19:
    print(teens[user])
# 20-90
if user >= 20 and user <= 99:
    tens_digit = user//10
    ones_digit = user % 10
    if ones_digit == 0:
        print(tens[tens_digit])
    else:
        # print(tens_digit, ones_digit)
        print(tens[tens_digit] + "-" + ones[ones_digit])
# 100-999
if user >= 100 and user <= 999:
    hundreds_digit = user//100
    # remove hundreds from input number
    hundreds_in_num = hundreds_digit * 100
    shortened = user - hundreds_in_num
    tens_digit = shortened//10
    ones_digit = shortened % 10

    if hundreds_digit >= 1 and tens_digit == 0 and ones_digit == 0:
        print(ones[hundreds_digit] + " hundred ")

    if tens_digit != 0 and ones_digit == 0:
        print(ones[hundreds_digit] + " hundred " + tens[tens_digit])

    if ones_digit >= 1:
        print(ones[hundreds_digit] + " hundred " +
              tens[tens_digit] + "-" + ones[ones_digit])

    # print(hundreds_digit[ones_digit]  tens_digit, ones[ones_digit] + "hundred")
    # print(ones[hundreds_digit] + " hundred " + tens[tens_digit] + "-" +
    #       ones[ones_digit])
