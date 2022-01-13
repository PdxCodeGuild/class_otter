# Lab 02: Average Numbers
# 01/06/2022

# Version 1

nums = [5, 0, 8, 3, 4, 1, 6]
total = 0


# loop over the indices and sum each member of the list
for i in range(len(nums)):
    total += nums[i]
    i += 1

# compute and output the average
average = total / len(nums)
print(average)




# Version 2

nums = []

while True:
    user = input('enter a number, or "done": ')

    if user != 'done':
        user = int(user)
        nums.append(user)

    else:
       average = sum(nums) / len(nums)
       print(average)
       break



# Extra Version to practice list comprehensions
