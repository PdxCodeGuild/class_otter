# *********************** #
#     BlackJack Advice    #
#     Strategy Engine     #
#       Version: 2.0      #
#   Author: Bruce Stull   #
#        2022-01-07       #
# *********************** #

from io import StringIO

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/04%20Blackjack%20Advice.md

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/02%20Exceptions%20%26%20Testing.md

# Create cards dictionary.
# Added functionality which accepts a '1' as input in addition to 'A'.
cards = {
    '1': 1,
    'A1': 1,
    'A11': 11,
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

# Use monkeypatch to test this.
# https://gist.github.com/GenevieveBuckley/efd16862de9e2fe7adfd2bf2bef93e02
def request_input(which_request = "Enter a value: "):
    '''Request input of card rank and return the upper-case card rank.'''
    while True:
        card = input(f"Please enter your {which_request} card: ").upper()
        if card in cards.keys():
            return card
        else:
            print("Please enter valid card rank.")
            continue

def test_request_input(monkeypatch):
    card_input = StringIO('a')
    monkeypatch.setattr('sys.stdin', card_input)
    # request_input('a') should be 'A'
    assert request_input() == 'A'
    
    card_input = StringIO('2')
    monkeypatch.setattr('sys.stdin', card_input)
    assert request_input() == '2'

# TODO: Add card validation, or error handling here.
def add_card_to_list(card, card_list = []):
    '''Add argument card to card list. Return the card list.'''
    card_list.append(card)
    return card_list

def test_add_card_to_list():
    assert add_card_to_list('j') == ['j']
    assert add_card_to_list('k',['2', '3']) == ['2', '3', 'k']
    assert add_card_to_list('K',['2', '3']) == ['2', '3', 'K']
    assert add_card_to_list('10',['1']) == ['1', '10']
    assert add_card_to_list('10',['7', '9']) == ['7', '9', '10']
    assert add_card_to_list('3',['j', '6']) == ['j', '6', '3']

# TODO: Maybe break out a function which only returns point value for a given card.
# TODO: Need to figure out way to make determine_points_of_cards_with_ace_accomodation() simpler.
# Maybe there is too much going on within the function?
# Maybe refactor determine_points_of_cards() first?

def determine_points_of_cards_with_ace_accomodation(card_list):
    '''Returns an integer point value if no Aces are present.'''
    '''Otherwise, returns a list of point values. Accomodates 'A' values of '1' and '11'.'''
    points_list = []
    # This case seems to work properly, so now only need to work on Aces present case.
    # No Aces present: Determine the integer point value when no Aces are present.
    if 'A' not in card_list and 'a' not in card_list:
        return determine_points_of_cards(card_list)
    
    # Aces present: Determine the point value list when Aces are present.
    else:
        list_of_point_values = [0, 0]
        # Iterate over list of cards.
        for card in card_list:
            # Add non-Ace values to all elements of points list.
            if card not in ['a', 'A']:
                list_of_point_values = add_card_value_to_all_list_elements(card, list_of_point_values)
            else:
                # We have a list list_of_point_values.
                # first_part = Add 1 to list of elements.
                first_part = add_card_value_to_all_list_elements('A1', list_of_point_values)
                # second_part = Add 11 to list of elements.
                second_part = add_card_value_to_all_list_elements('A11', list_of_point_values)
                # first_part.extend(second_part)
                list_of_point_values = first_part.extend(second_part)
        return list_of_point_values

        # return f"\n'A' or 'a' present: {card_list}"

def test_determine_points_of_cards_with_ace_accomodation():
    ### Temporary tests ###
    # assert determine_points_of_cards_with_ace_accomodation(['A','3','4']) == [8, 18]
    ### Permanent tests ###
#     assert determine_points_of_cards_with_ace_accomodation(['a','k','j']) == 21 or 31
    assert determine_points_of_cards_with_ace_accomodation(['2','3','4']) == 9
    assert determine_points_of_cards_with_ace_accomodation([' ','2','3']) == 5
    assert determine_points_of_cards_with_ace_accomodation(['5','%','2']) == 7
    assert determine_points_of_cards_with_ace_accomodation(['9','2','?']) == 11
    assert determine_points_of_cards_with_ace_accomodation(['9','2','j']) == 21
    assert determine_points_of_cards_with_ace_accomodation(['9','q','?']) == 19
    assert determine_points_of_cards_with_ace_accomodation(['k','2','?']) == 12
    assert determine_points_of_cards_with_ace_accomodation(['q','k','j']) == 30
    assert True == True

def add_card_value_to_all_list_elements(card, list_of_point_values = [0]):
    '''Accepts card and list of integers. Returns list with the point value of the card added to all list members.'''
    for i in range(len(list_of_point_values)):
        list_of_point_values[i] += cards[card.upper()]
    return list_of_point_values

def test_add_card_value_to_all_list_elements():
    assert add_card_value_to_all_list_elements('2', [1,2]) == [3,4]
    assert add_card_value_to_all_list_elements('K', [3,5,7]) == [13,15,17]
    assert add_card_value_to_all_list_elements('j', [3,5,7]) == [13,15,17]
    assert add_card_value_to_all_list_elements('J', [3,5,7,2]) == [13,15,17,12]
    assert add_card_value_to_all_list_elements('7', [3,5,7]) == [10,12,14]

def determine_points_of_cards(card_list):
    '''Returns the point value of the sum of the argument card list.'''
    points = 0
    for card in card_list:
        # Experiment with error handling.
        # Handle inputs not in dictionary.
        try:
            points += cards[card.upper()]
        except KeyError:
            points += 0
    return points

def test_determine_points_of_cards():
    assert determine_points_of_cards(['2','3','4']) == 9
    assert determine_points_of_cards(['A','3','4']) == 8
    assert determine_points_of_cards([' ','2','3']) == 5
    assert determine_points_of_cards(['5','%','2']) == 7
    assert determine_points_of_cards(['9','2','?']) == 11
    assert determine_points_of_cards(['9','2','J']) == 21
    assert determine_points_of_cards(['9','Q','?']) == 19
    assert determine_points_of_cards(['K','2','?']) == 12
    assert determine_points_of_cards(['Q','K','J']) == 30

def advise(points):
    '''Accepts arguments of points sum and returns the advise string.'''
    if points > 21:
        advice = "Already Busted"
    elif points == 21:
        advice = "Blackjack!"
    elif points >= 17:
        advice = "Stay"
    else:
        advice = "Hit"
    return advice

def test_advise():
    assert advise(22) == "Already Busted"
    assert advise(21) == "Blackjack!"
    assert advise(18) == "Stay"
    assert advise(17) == "Stay"
    assert advise(12) == "Hit"

def results_string(points):
    '''Accepts argument of card points sum and returns a sting of the points value and the advise.'''
    results = f"{points} {advise(points)}"
    return results

def test_results_string():
    assert results_string(22) == "22 Already Busted"
    assert results_string(21) == "21 Blackjack!"
    assert results_string(18) == "18 Stay"
    assert results_string(17) == "17 Stay"
    assert results_string(12) == "12 Hit"

def main():    
    card_requests =['first', 'second', 'third']
    
    for request in card_requests:
        card = request_input(request)
        card_list = add_card_to_list(card)
        points = determine_points_of_cards(card_list)

    print(f'''
    {points}: {advise(points)}
    ''')

    # points_list = []

    # print(f'''
    # Points list: {points_list}
    # ''')
        

# main()
