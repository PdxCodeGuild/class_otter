#Lab 6 Credit Card Validator
credit_card = input("Enter your 16 digit credit card number, no spaces: ")

# convert string to int list
cc_num = [eval(_) for _ in credit_card]

#slice off and remove check digit
cc_num_check  = cc_num[-1]
del cc_num[-1]

#reverse the list
cc_num.reverse()

#double odd numbers
odds = cc_num[:]
odds[::2] = [o*2 for o  in odds[::2]]

#subtract 9 if over 9
for x in range(len(cc_num)):
    if odds[x] > 9:
        odds[x] -=9

#add it up
total = sum(odds)

#validate second digit against check digit
sec_dig = total  % 10

print("Your Credit Card Number is: ", credit_card)
print("Your Check Digit is: ", cc_num_check)
print("The Total of the Digits is: ", total)
print("The Second Digit of the Total is: ", sec_dig)
if cc_num_check == sec_dig:
    print("This is a valid credit card number!")
else:
    print("Invalid Card Number!!")