print('\nWelcome to the BlackJack Advisor\n')

crd_val= {'A':1, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, "K":10 }

usr_1 = input ('\nWhat is your first card?\n').upper()

usr_2 = input ('\nWhat is your second card?\n').upper()

usr_3 = input ('\nWhat is your third card?\n').upper()

usr_point = crd_val[usr_1] + crd_val[usr_2] + crd_val[usr_3]

if usr_point <=17:
    print(f'\n{usr_point}, HIT')

elif usr_point >= 17 and usr_point < 21:
    print(f'\n{usr_point}, STAY')

elif usr_point == 21:
    print(f'\n{usr_point}, BLACKJACK!')

elif usr_point > 21:
    print(f'\n{usr_point}, ALREADY BUSTED!')