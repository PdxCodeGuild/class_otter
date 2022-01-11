#Lab06.py - Credit Card Validation - Scott Madden

#Request credit card input
cc = input("Please enter a 16 digit credit card number without spaces")
nums = [eval(x) for x in cc] # Convert string to a List
print("You entered:" , nums)
nums_check = nums[-1] #slice off last number to be used as check number
print("Your Check Digit is:" , nums_check)
nums.reverse() #reverse List
print( "Your numbers reversed" , nums)
#double second number (left to right)
every_second = nums[:]
every_second[::2] =[x*2 for x in every_second[::2]]
#nums[item * 2 if index % 2 == 0 else item for index, item in enumerate(1st)]
print("Every second number doubled from left to right:" , every_second)
#nums
 


# [int(x) for x in cc]
# cc_list = cc.split()
