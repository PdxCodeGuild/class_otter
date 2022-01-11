import random

def pick6():
    return [random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99) ,
    random.randint(1,99) ,
    random.randint(1,99)]

# winning_numbers = pick6()

def this_guess():
    return [random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99),
    random.randint(1,99) ,
    random.randint(1,99) ,
    random.randint(1,99)]

# guessed_numbers = this_guess()

# print(winning_numbers)
# print(guessed_numbers)

def matching_num(winning_numbers, guessed_numbers):
    match_counter = 0
    for num in range(6):

        if winning_numbers[num] == guessed_numbers[num]:
            match_counter += 1

    return match_counter

 

def payout(number_of_matches):
    if number_of_matches == 0:
        return 0
    elif number_of_matches == 1:
        return 4
    elif number_of_matches == 2:
        return 100
    elif number_of_matches == 3:
        return 50000
    elif number_of_matches == 4:
        return 1000000
    elif number_of_matches == 5:
        return 25000000




def main():
    money_total = 0
    pure_winnings = 0
    expenses = 0
    loop_counter = 0
    while loop_counter < 100000:
        expenses -= 2
        winning_numbers = pick6()
        guessed_numbers = this_guess()
        number_of_matches = matching_num(winning_numbers,guessed_numbers)
        pure_winnings += payout(number_of_matches)
        loop_counter += 1
        print(pure_winnings, expenses)
    print(f'you baught 100,000 tickets . your ROI is {(pure_winnings-expenses)/expenses}')

main()