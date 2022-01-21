conversion = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
              7: "seven", 8: "eight", 9: "nine"}

conversion_2 = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                17: "seventeen", 18: "eighteen", 19: "nineteen"}

conversion_3 = {20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
                100: "hundred"}


def nums_to_phrase(user_num):
    for i in user_num:
        if user_num == i//10:
            return conversion_2
        elif user_num == i % 10:
            return conversion_3


user = int(input("please enter a number: "))

if user == 0:
    print(conversion[0])
elif user == 1:
    print(conversion[1])
elif user == 2:
    print(conversion[2])
elif user == 3:
    print(conversion[3])
elif user == 4:
    print(conversion[4])
elif user == 5:
    print(conversion[5])
elif user == 6:
    print(conversion[6])
elif user == 7:
    print(conversion[7])
elif user == 8:
    print(conversion[8])
elif user == 9:
    print(conversion[9])


print(nums_to_phrase(user))
