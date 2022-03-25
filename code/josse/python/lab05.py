import random

def generate_ticket():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))
        
    return nums


# winning_numbers = generate_ticket()


# print(winning_numbers)

# def my_ticket():
#     for i in range(6):
#         my_numbers.append(random.randint(1,99))
#     return my_numbers
        
# my_numbers = []

# my_numbers = my_ticket()

# print(my_numbers)



def find_matches(winning_numbers,my_numbers):
    matches = 0
    for i in range(len(winning_numbers)):
        if winning_numbers[i] == my_numbers[i]:
            matches += 1
    return matches
  

# print(find_matches(winning_numbers,my_numbers))

# match_finder = find_matches(winning_numbers,my_numbers)


# def add_to_balance(match):
#     balance = 0 

# test_three_numbers = [43,77,22,5,54]

# test_three_numbers_compare = [5,88,22,43,22]

# testing = find_matches(test_three_numbers,test_three_numbers_compare)

# print(testing)


# call winning ticket function and assaign winning ticket to variable. 

winning_per_match = {
        0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000
}

winning_ticket = generate_ticket()

balance = 0

user_choice_of_tickets = input("how many tickets would you like to purchase? ")
number_of_tickets_to_buy = int(user_choice_of_tickets)

final_balance = 0

for _ in range(number_of_tickets_to_buy):
    my_ticket = generate_ticket()
    balance -= 2 
    number_of_matches = find_matches(winning_ticket,my_ticket)
    final_balance += winning_per_match[number_of_matches]

print(final_balance) 

#return on investment
earnings = final_balance 

expenses = number_of_tickets_to_buy * 2

roi = (earnings - expenses)/expenses
print(f"this is my earnings:{earnings}, this is my expenses:{expenses}, this is my return on investment:{roi}")