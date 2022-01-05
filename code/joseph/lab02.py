#Average Numbers
#Version 1
#nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
#for num in nums:
#    print(num)

# loop over the indices
#for i in range(len(nums)):
#    print(nums[i])

nums = [5, 0, 8, 3, 4, 1, 6]
for num in nums:
    print(num)
for i in range(len(nums)):
    print(nums[i])
average = sum(nums) / len(nums)
print('The average is ' + str(round(average, 2)))