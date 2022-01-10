
# LAB 3 VERSION 1 & 2 ## DRAFT ##

usr_num = input('\nEnter a number to convert into a phrase:\n')

usr_num = int(usr_num)

ones_digit = usr_num%10

tens_digit = (usr_num//10)%10

hund_digit = (usr_num//100)

print (ones_digit)
print (tens_digit)
print (hund_digit)

ones = {
    0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    
teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

tens = {20:'twenty', 30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}


if usr_num < 10:
    num_cnvr_wrd = ones[usr_num]
    print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

elif usr_num >= 10 and usr_num <= 19: 
    num_cnvr_wrd = teens[usr_num]
    print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

elif usr_num >= 20 and usr_num <= 99:
    
    if ones_digit == 0 :
        num_cnvr_wrd = tens[usr_num]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    else: 
        num_cnvr_wrd = tens[tens_digit*10] + '-' + ones[ones_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

elif usr_num >= 100 and usr_num <=999:
    
    if ones_digit == 0 and tens_digit ==0 :
        num_cnvr_wrd = ones[hund_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}-hundred')
    
    elif tens_digit >=1 and tens_digit <=9:
        num_cnvr_wrd = ones[hund_digit]+ '-hundred' + ' and ' + tens[tens_digit*10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 110 and usr_num <= 119:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')

    elif usr_num >= 210 and usr_num <= 219:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 310 and usr_num <= 319:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 410 and usr_num <= 419:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 510 and usr_num <= 519:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 610 and usr_num <= 619:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 710 and usr_num <= 719:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 810 and usr_num <= 819:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    elif usr_num >= 910 and usr_num <= 919:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + teens[ones_digit+10]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')
    
    else:
        num_cnvr_wrd = ones[hund_digit] + '-hundred and ' + ones[ones_digit]
        print(f'\n{usr_num} is converted into: {num_cnvr_wrd}')






        
    
    