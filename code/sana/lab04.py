fcard = input("What's your first card? ")
scard = input("What's your second card? ")
tcard = input("What's your third card? ")
cards = {
    'A' : 1,
    'K' : 10,
    'Q' : 10,
    'J' : 10,
    '2': 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '10' : 10 
}
def blackjack(f, s, t):
    fc = cards[f]
    sc = cards[s]
    tc = cards[t]
    total = int(fc) + int(sc) + int(tc)
    return total
# print(blackjack(fcard, scard, tcard))
result = blackjack(fcard, scard, tcard) 
if result == 21:
    print("21 Blackjack!")
elif result < 17:
    print(f'{result} Advising to Hit')
elif result >= 17 and result < 21:
    print(f'{result} Advising to Stay')
elif result > 21:
    print(f'{result} Already Busted...')