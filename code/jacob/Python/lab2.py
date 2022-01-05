"""

Lab 2: Average Numbers

"""


import string


# wanted to created my own adding function


def summ(numbers):
    
    answer = 0    
    
    for num in numbers:
        
        answer += num
          
    return answer


"""

Version 1

"""

# take in the numbers list to add and get the average

nums = [5, 0, 8, 3, 4, 1, 6]

count = 0
for item in nums:
    count += 1

average = round(((summ(nums)) / count ), 4)

print(nums)
print(summ(nums))
print("Average: ", average)

"""

Version 2

"""

# changed the functionality to include taking numbers from a user and then finding their average

numbers = []
numbers.append(int(input("What is the first number you want to add?: ")))

check = 'yes'
while check == 'yes':

    if check == 'yes':
        numbers.append(int(input("What is the next number you want to add?: ")))
        
        if check == 'yes':
            check = input("Do you want to add another number type yes or no?: ")


x = 0
for item in numbers:
    x += 1

y = round(((summ(numbers)) / x ), 4)


print(numbers)
print(summ(numbers))
print("Average: ", y)
