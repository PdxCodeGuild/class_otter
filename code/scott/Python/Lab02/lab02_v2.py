#Lab 02 Average Nunmbers Version 2 - Scott Madden
nums = []
entry = True
while entry:
    num = input(""" please enter a number between 0 and 5 to continue
    or enter done to finish: """)
    if num == 'done':
        entry = False
    else:
        nums.append(int(num))
        entry = True

def sum(nums): #defining the function 'sum' with one parameter 'numbers'
    add = 0 
    for num in nums:
        add = add + num
    return add

x = sum(nums) #call the function
avg = x / len(nums)
print ("your average is:")
print (avg)




