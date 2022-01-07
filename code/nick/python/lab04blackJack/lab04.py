playing_cards =  {'A': 1, '1': 1 ,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10,'Q': 10}

# def black_jack(a,b,c):
#     a = playing_cards[first_card]

first_card = input('what is your first card? ')

second_card = input('whats the second card? ')

third = input('whats the third card? ')

# black_jack(a=first_card,b= second_card,c= third)

# black_jack(playing_cards['J'],playing_cards['A'])

def black_Jack(a,b,c):
    total = a+b+c
    if total == 21:
        print('Black Jack!')
    elif 21< total >= 17:
        print('Stay and Hold')
    elif total <17:
        print('Hit')
    elif total> 21:
        print('busted')





black_Jack(playing_cards[first_card],playing_cards[second_card], playing_cards[third])



