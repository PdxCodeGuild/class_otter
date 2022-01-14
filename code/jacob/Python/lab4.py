"""
Lab 4: Blackjack Advice

"""

"""
Version 1
Version 2 has been worked in to complete the optional portion.

"""
print()

points = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
'10': 10, 'J': 10, 'Q': 10, 'K': 10, 'none': 0, 'q': 10, 'k': 10, 'j': 10, 'a': 1}

card1 = input('What is your first card? ')
card2 = input('what is your second card? ')
card3 = input('what is your third card or type "none"? ')


def score(a, b, c):
    x = points[a] + points[b] + points[c]
    return x

advice = score(card1, card2, card3)

while advice <= 21:
      
    
    if points[card1] == 10 and card2 == 'A' or 'a':
        print('21 Blackjack!')
        break
   
    elif advice < 17:
        print(f' {advice} Hit')

    elif advice >= 17 and advice < 21:
        print(f' {advice} Stay')
        break
    
    elif advice > 21:
        print(f' {advice} Busted')

    else:
        print(f' {advice} Blackjack!')
        break
    
    if advice == 10 and card4 == 'A' or 'a':
        print(f'{advice} Blackjack')
        break

    card4 = input('What is your next card? ')
    advice += points[card4]       


print()       