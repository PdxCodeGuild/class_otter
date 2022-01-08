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

# Not sure how to test this.
# https://gist.github.com/GenevieveBuckley/efd16862de9e2fe7adfd2bf2bef93e02
def request_input(which_request = "Enter a value: "):
    '''Request input of card rank and return the card.'''
    card = input(f"Please enter your {which_request} card: ")
    return card

def test_request_input(monkeypatch):
    card_input = StringIO('a')
    monkeypatch.setattr('sys.stdin', card_input)
    assert request_input() == 'a'
    
    card_input = StringIO('2')
    monkeypatch.setattr('sys.stdin', card_input)
    assert request_input() == '2'

def add_card_to_list(card, card_list = []):
    '''Add argument card to card list. Return the card list.'''
    card_list.append(card)
    return card_list

def test_add_card_to_list():
    assert add_card_to_list('j') == ['j']
    assert add_card_to_list('k',['2', '3']) == ['2', '3', 'k']
    assert add_card_to_list('10',['1']) == ['1', '10']
    assert add_card_to_list('10',['7', '9']) == ['7', '9', '10']
    assert add_card_to_list('3',['j', '6']) == ['j', '6', '3']

# def create_optional_points_of_cards(card_list):
#     '''Accepts argument of card list. Returns a list of one or more point values when Aces are present.'''
#     points = [0, 0, 0, 0, 0, 0, 0, 0]
#     for card in card_list:
#         if card not in ['A']:
#             # Add card value to all slots in list.
#             for score in points:
#                 score += cards[card.upper()]
#     return points

# def test_create_optional_points_of_cards():
#     card_list = ['2']
#     print(card_list)
#     assert create_optional_points_of_cards(card_list) == [2, 2, 2, 2, 2, 2, 2, 2]

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
    assert determine_points_of_cards([' ','2','3']) == 5
    assert determine_points_of_cards(['5','%','2']) == 7
    assert determine_points_of_cards(['9','2','?']) == 11
    assert determine_points_of_cards(['9','2','j']) == 21
    assert determine_points_of_cards(['9','q','?']) == 19
    assert determine_points_of_cards(['k','2','?']) == 12
    assert determine_points_of_cards(['q','k','j']) == 30

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
    
    card_list = []
    for request in card_requests:
        card = request_input(request)
        card_list = add_card_to_list(card, card_list)
        points = determine_points_of_cards(card_list)

    print(f'''
    {points}: {advise(points)}
    ''')

main()

# This 'print()' function is not run during pytest.
# Correction: The function may 'run' but there is nothing printed to console.
print("Tests are probably complete.")

# # This non-declared variable inside 'print()' is attempted to run during pytest, so pytest errored out.
# print(a_non_declared_variable)

# ___________________________________________________________________________________ ERROR collecting lab04v20.py ___________________________________________________________________________________ 
# lab04v20.py:148: in <module>
#     print(a_non_declared_variable)
# E   NameError: name 'a_non_declared_variable' is not defined
# ----------------------------------------------------------------------------------------- Captured stdout ------------------------------------------------------------------------------------------ 
# Tests are probably complete.
# ===================================================================================== short test summary info ====================================================================================== 
# ERROR lab04v20.py - NameError: name 'a_non_declared_variable' is not defined
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
# ========================================================================================= 1 error in 0.13s ========================================================================================= 
# PS C:\Users\Bruce\Programming\class_otter\code\bruce\week_01>


# # Only the calling of 'main()' needs to commented out to successfully run tests.
# # So, it seems, any code or function calls will run when pytest is run.
# # i.e. Any code of function calls which are not inside of other function calls will run.
# def main():
#     print("Main function has run.")

# main()