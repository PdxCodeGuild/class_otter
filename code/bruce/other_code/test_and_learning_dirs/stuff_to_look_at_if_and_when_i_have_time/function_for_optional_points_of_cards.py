# print('2' not in ['A'])

# Create cards dictionary.
cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

print(cards['2'.upper()], type(cards['2'.upper()]))


def create_optional_points_of_cards(card_list):
    '''Accepts argument of card list. Returns a list of one or more point values when Aces are present.'''
    # print(f"card_list: {card_list}")
    points_list = [0, 0, 0, 0, 0, 0, 0, 0]
    # print(f"points_list: {points_list}")

    for card in card_list:
        print(f"card: {card} {type(card)}")
        if card not in ['A']:
            print(f"{card} not in 'A'")
            for i in range(len(points_list)):
                points_list[i] += cards[card.upper()]
        else:
            print(f"{card} in 'A'")
    return points_list

cards_list = ['2', 'A', 'K', '7']
print(create_optional_points_of_cards(cards_list))

