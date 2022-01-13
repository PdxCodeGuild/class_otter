#Lab06.py - Credit Card Validation - Scott Madden

#Request credit card input
cc = input("Please enter a 16 digit credit card number without spaces")
nums = [eval(_) for _ in cc] # Convert string to a List
print("You entered:" , nums)

nums_check = nums[-1] #slice off last number to be used as check number
print("Your Check Digit is:" , nums_check)
del nums[-1]
# print(nums)
nums.reverse() #reverse List
print( "Your numbers reversed" , nums)

#double second number (left to right)
# for i in range(0, len(nums), 2):
#     nums[1] *= 2
every_second = nums[:]
every_second[::2] =[x*2 for x in every_second[::2]]
#nums[item * 2 if index % 2 == 0 else item for index, item in enumerate(1st)]
print("Every second number doubled from left to right:" , every_second)

for i in range(len(nums)):
    if every_second[i] > 9:
        every_second[i] -= 9


result = sum(every_second) # sum all values
second_digit = result % 10 #Second digit for validation check

print('Your Credit Card Number is:' , cc)
print('The Sum of the numbers is:' , result)
print('The second digit is:', second_digit) 
print('The Check Number to Compare for validation is:', nums_check)
if nums_check == second_digit:
    print('valid check')
else:
    print('Invalid check')



