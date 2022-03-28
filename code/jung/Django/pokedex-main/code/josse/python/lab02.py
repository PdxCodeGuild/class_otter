'''nums = [5, 0, 8, 3, 4, 1, 6]

for num in nums:
   print(num)

counter = 0

for i in range(len(nums)):
    counter += nums[i]

average = counter / nums[i]

print(average)'''

#----------------------------------------------------------------------#


nums = []
#for loop to achieve multiple entries 
for i in range(6):

    number = input("please enter a number or done:  ") 
    if number == "done":
        print("done") 
        break 

    nums.append(float(number))

thesum = 0

for number in nums:
    thesum += number

total = len(nums) 

average= thesum / total

print(average)

