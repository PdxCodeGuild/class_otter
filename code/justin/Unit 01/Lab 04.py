# Full Stack Bootcamp - Unit 01 Lab 04
# Justin Hammond, 01/06/2022


'''
Write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask
the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each
card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are
worth 1. Use the following rules to determine the advice:

    Less than 17, advise to "Hit"
    Greater than or equal to 17, but less than 21, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"

Print out the current total point value and the advice.
'''


playing_card_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

ordinal_name_map = {
    1: "first",
    2: "second",
    3: "third"
}

advice_strings = ['Hit', 'Stay', 'Blackjack!', 'Already Busted']


def get_card(card_ordinal):
    card = input(f"What's your {ordinal_name_map[card_ordinal]} card? ").upper()

    if card.isdigit():
        card = int(card)
        if card > 1 and card < 11:
            return str(card)
        return None
    
    if card == 'A' or card == 'ACE':
        return 'A'
    elif card == 'J' or card == 'JACK':
        return 'J'
    elif card == 'Q' or card == 'QUEEN':
        return 'Q'
    elif card == 'K' or card == 'KING':
        return 'K'
    
    return None

def get_hand_value(cards):
    result = 0
    for card in cards:
        result += playing_card_values[card]
    return result

def test_get_hand_value():
    assert get_hand_value(['A', '5', '4']) == 10
    assert get_hand_value(['10', '9', '2']) == 21
    assert get_hand_value(['K', 'Q', 'A']) == 21
    assert get_hand_value(['K', 'Q', 'J']) == 30

def get_advice(hand_value):
    if hand_value < 3:
        return None
    elif hand_value < 17:
        return advice_strings[0]
    elif hand_value < 21:
        return advice_strings[1]
    elif hand_value == 21:
        return advice_strings[2]
    elif hand_value > 21:
        return advice_strings[3]

    return None

def test_get_advice():
    assert get_advice(-37) == None

    assert get_advice(3) == 'Hit'
    assert get_advice(4) == 'Hit'
    assert get_advice(5) == 'Hit'
    assert get_advice(6) == 'Hit'
    assert get_advice(7) == 'Hit'
    assert get_advice(8) == 'Hit'
    assert get_advice(9) == 'Hit'
    assert get_advice(10) == 'Hit'
    assert get_advice(11) == 'Hit'
    assert get_advice(12) == 'Hit'
    assert get_advice(13) == 'Hit'
    assert get_advice(14) == 'Hit'
    assert get_advice(15) == 'Hit'
    assert get_advice(16) == 'Hit'

    assert get_advice(17) == 'Stay'
    assert get_advice(18) == 'Stay'
    assert get_advice(19) == 'Stay'
    assert get_advice(20) == 'Stay'

    assert get_advice(21) == 'Blackjack!'

    assert get_advice(22) == 'Already Busted'
    assert get_advice(23) == 'Already Busted'
    assert get_advice(24) == 'Already Busted'
    assert get_advice(25) == 'Already Busted'
    assert get_advice(26) == 'Already Busted'
    assert get_advice(27) == 'Already Busted'
    assert get_advice(28) == 'Already Busted'
    assert get_advice(29) == 'Already Busted'
    assert get_advice(30) == 'Already Busted'


def main():
    card_list = []
    for index in range(3):
        card_list.append(get_card(index+1))
    
    hand_value = get_hand_value(card_list)

    advice = get_advice(hand_value)

    print(f"\n{hand_value}: {advice}")

main()