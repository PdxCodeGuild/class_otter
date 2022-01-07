# *********************** #
#     BlackJack Advice    #
#     Strategy Engine     #
#       Version: 1.0      #
#   Author: Bruce Stull   #
#        2022-01-07       #
# *********************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/04%20Blackjack%20Advice.md

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/02%20Exceptions%20%26%20Testing.md

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

def determine_points_of_cards(card_list):
    '''Returns the point value of the sum of three argument card ranks.'''
    '''TODO: Change arguments from three individual args to one list arg. The list can be more than three elements long.'''
    points = 0
    for card in card_list:
        # Experiment with error handling.
        # Handle inputs not in dictionary.
        try:
            points += cards[card]
        except KeyError:
            points += 0
    return points

def test_determine_points_of_cards():
    assert determine_points_of_cards(['2','3','4']) == 9
    assert determine_points_of_cards([' ','2','3']) == 5
    assert determine_points_of_cards(['5','%','2']) == 7
    assert determine_points_of_cards(['9','2','?']) == 11

def request_input_return_points(card_requests =['first', 'second', 'third']):
    '''Requests user input of cards and returns blackjack point value of the hand.'''
    card_values = []
    for item in card_requests:
        card_values.append(input(f"Please enter your {item} card rank: "))
    return determine_points_of_cards(card_values)

# # TODO: Learn how to test function which have user input.
# def test_request_input_return_points():
#     assert request_input_return_points() == 9 # I have to use -s pytest option and manually input three '3' rank cards.

def advise(points):
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
    results = f"{points} {advise(points)}"
    return results

def test_results_string():
    assert results_string(22) == "22 Already Busted"
    assert results_string(21) == "21 Blackjack!"
    assert results_string(18) == "18 Stay"
    assert results_string(17) == "17 Stay"
    assert results_string(12) == "12 Hit"

def main():
    # Request input and store points in variable for use later.
    points = request_input_return_points()
    
    print(f'''
    {points}: {advise(points)}
    ''')

main()