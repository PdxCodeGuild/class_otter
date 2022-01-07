# Lab 02: Average Numbers

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
# for num in nums:
#     print(num)

# Version 1 

# loop over the indices and sum each member of the list
for i in range(len(nums)):
    sum += nums[i]
    i += 1

# compute and output the average
average = sum / len(nums)
print(average)

# Version 2

nums = []

user = input('enter a number, or "done": ')
while user != 'done':
        if user == 'done':
            # average the current nums list
            print('placeholder avg')
        else:
            nums.append(user)