
# LAB 3 VERSION 1 & 2 ## DRAFT ##

usr_num = input('\nEnter a number to convert into a phrase:\n')

usr_num = int(usr_num)

ones_digit = usr_num%10

tens_digit = (usr_num//10)%10

hund_digit = usr_num//100

print (ones_digit)
print (tens_digit)
print (hund_digit)

num_wrd_ones = {
    0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    
num_wrd_teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

num_wrd_tens = {20:'twenty', 30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

if usr_num < 10:
    num_cnvr_wrd = num_wrd_ones[usr_num]
    print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

elif usr_num >= 10 and usr_num <= 19: 
    num_cnvr_wrd = num_wrd_teens[usr_num]
    print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

elif usr_num >= 20 and usr_num <= 99:
    
    if ones_digit == 0 :
        num_cnvr_wrd = num_wrd_tens[usr_num]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    else: 
        num_cnvr_wrd = num_wrd_tens[tens_digit*10] + '-' + num_wrd_ones[ones_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

elif usr_num >= 100 and usr_num <=999:
    
    if ones_digit == 0 and tens_digit == 0 :
        num_cnvr_wrd = num_wrd_ones[hund_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}-hundred')
    
    elif tens_digit == num_wrd_teens:
        num_cnvr_wrd = num_wrd_ones[hund_digit] + '-hundred and ' + num_wrd_teens[tens_digit + ones_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    else:
        num_cnvr_wrd = num_wrd_ones[hund_digit] + '-hundred and ' + num_wrd_ones[ones_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')






        
    
    