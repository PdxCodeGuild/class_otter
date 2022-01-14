"""
Lab 6: Credit Card Validation
"""

def convert(card):
    card = card.split()
    for num in range(len(card)):
        card[num] = int(card[num])

    return card    

def numspace(num):
    return ' '.join(num)

def doublenum(list):
    for num in range(0, len(list), 2):
        list[num] *= 2
    return list

def subtract_nine(list):
    for num in range(len(list)):
        if list[num] > 9:
            list[num] -= 9
    return list

def checker(a, b):
    if a == b:
        return True
    else:
        return False
print()
creditcard = input('Please enter your credit card#: ')

def card_check(creditcard):
    creditcard = numspace(creditcard)
    print(creditcard)
    cardint = convert(creditcard)
    print(cardint)
    check_digit = cardint.pop()
    print(cardint)
    cardint.reverse()
    print(cardint)
    double = doublenum(cardint)
    print(double)

    subnine = subtract_nine(cardint)
    sum_num = sum(subnine)
    print(subnine)
    print(sum_num)
    print(check_digit)

    counter_check = sum_num % 10
    print(checker(check_digit, counter_check))
    return check_digit == counter_check    

card_check(creditcard)
print()    