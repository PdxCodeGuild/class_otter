nums = [5, 0, 8, 3, 4, 1, 6]

# sum = sum(nums)
# avrg = sum/len(nums)
# print (round(avrg,2))

total = 0

###### EITHER FOR LOOP ######

# for num in nums:
#     total+= num
#     #print (num)

# avrg = round(total/len(nums),2)

# print(f'The average list of numbers is : {avrg}')

for i in range(len(nums)):
    total +=nums[i]
    #print (nums[i])

avrg = round(total/len(nums),2)

print(f'The average list of numbers is : {avrg}')

 