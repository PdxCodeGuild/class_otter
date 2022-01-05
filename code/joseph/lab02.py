#Average Numbers
#Version 1

#nums = [5, 0, 8, 3, 4, 1, 6]
#for num in nums:
#    print(num)
#for i in range(len(nums)):
#    print(nums[i])
#average = sum(nums) / len(nums)
#print('The average is ' + str(round(average, 2)))
#version 1
#version 2
nums = []
while True:
    num = input('enter a number or done: ')
    if num == 'done':
        break
    nums.append(int(num))
print(nums)
average = sum(nums) / len(nums)
print('The average is ' + str(round(average, 2)))
#version 2