user_creditcard = input('enter your credit card number ')


credit_card_digits = [int(number) for number in str(user_creditcard)]

def converter(input):
    input.pop(15)
    input = input[::-1]
    return input

card_reversed = converter(credit_card_digits)


doubled_odds = [n * 2 for n in card_reversed]
# def double_other_digits(input):
#     numbers = input
#     doubled_odds = [n * 2 for n in numbers if n % 2 == 0]
#     print(input)
#     print(doubled_odds)
    
    

print(card_reversed)
print(doubled_odds)
# def credit_card_input(input):


# convert_slice_reverse = credit_card_input(user_creditcard)
