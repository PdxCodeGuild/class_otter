'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*      Lab 02(V2) - Average Numbers         *
*            05/January/2022                *
*                                           *
*********************************************
'''
nums = []
def sum(nums): #defining the function 'sum' with one parameter 'numbers'
    add = 0 
    for num in nums:
        add = add + num
    return add

entry = True
while entry:
    num = input(""" please enter a number between 0 and 5 to continue
    or enter done to finish: """)
    if num == 'done':
        entry = False
    else:
        nums.append(int(num))
        entry = True

x = sum(nums) #call the function
avg = x / len(nums)
print ("your average is:")
print (avg)




