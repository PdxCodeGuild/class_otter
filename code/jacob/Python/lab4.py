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

if (points[card1] == 10 and card2 == 'A') or (card1 == 'A' and points[card2] == 10):
    advice = 21
    print('21 Blackjack!')
       
    
elif (points[card1] == 10 and card2 == 'a') or (card1 == 'a' and points[card2] == 10):
    advice = 21
    print('21 Blackjack!')    

elif advice > 21:
    print(f'{advice} Busted')

elif advice == 21:
    print(f'{advice} Blackjack')

while advice < 21:
  

    if advice < 17:
        print(f' {advice} Hit!')

    elif advice >= 17 and advice < 21:
        print(f' {advice} Stay!')
        break
    
    elif advice > 21:
        print(f' {advice} Busted!')


    card4 = input('What is your next card? ')
    
    if advice == 10 and card4 == 'A':
        print(f'{advice} Blackjack!')
        break
 
    elif advice == 10 and card4 == 'a':
        print(f'{advice} Blackjack!')
        break
    
    elif (advice + points[card4]) > 21:
        print(f'{(advice + points[card4])} Busted')

    elif (advice + points[card4]) == 21:
        print(f'{(advice + points[card4])} Blackjack!') 
    
    advice += points[card4]       


print()       