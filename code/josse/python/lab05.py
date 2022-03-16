import random

def winning_ticket():
    for i in range(6):
        nums.append(random.randint(1, 99))
        
    return nums

nums = []

winning_numbers = winning_ticket()


print(winning_numbers)

def my_ticket():
    for i in range(6):
        my_numbers.append(random.randint(1,99))
    return my_numbers
        
my_numbers = []

my_numbers = my_ticket()

print(my_numbers)

balance = 0 

match = 0

def find_matches(winning_numbers,my_numbers):
if my_numbers==winning_numbers:
        match += 1

return match

print(find_matches(winning_numbers,my_numbers))
