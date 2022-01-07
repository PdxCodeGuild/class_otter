# x = 67

# tens_digits = x//10

# ones_digits = x%10



usr_num = input('\nEnter a number to convert into a phrase:\n')

usr_num = int(usr_num)

tens_digit = usr_num//10

ones_digit = usr_num%10

print (tens_digit)
print (ones_digit)



num_wrd = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'7',8:'eight',9:'nine',10:'ten',
    11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fiftenn',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
    20:'twenty', 30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

num_cnvr_wrd = num_wrd[usr_num]

print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')