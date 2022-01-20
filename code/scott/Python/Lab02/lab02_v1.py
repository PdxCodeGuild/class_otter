#Lab 02 Average Nunmbers version_1 - Scott Madden
nums = [5, 0, 8, 3, 4, 1, 6]

def sum(nums): #defining the function 'sum' with one parameter 'numbers'
    add = 0 
    for num in nums:
        add = add + num
    return add

x = sum(nums) #call the function
avg = x / len(nums)
print (avg)