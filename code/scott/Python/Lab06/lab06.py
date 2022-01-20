#Lab06.py - Credit Card Validation - Scott Madden

# Request credit card input
cc = input("Please enter a 16 digit credit card number without spaces")
nums = [eval(_) for _ in cc] # Convert string to a List
nums_check = nums[-1] #slice off last number to be used as check number
del nums[-1]#remove check number
nums.reverse() #reverse List
every_second = nums[:] # Every second number doubled from left to right
every_second[::2] =[x*2 for x in every_second[::2]]

for i in range(len(nums)):
    if every_second[i] > 9:
        every_second[i] -= 9

result = sum(every_second) # sum all values
second_digit = result % 10 #Second digit for validation check

print('Your Credit Card Number is:' , cc)
print("Your Check Digit is:" , nums_check)
print('The Sum of the Numbers is:' , result)
print('The Second Digit is:', second_digit) 
print('The Check Number to Compare for Validation is:', nums_check)
if nums_check == second_digit:
    print('Valid check')
else:
    print('Invalid check')



