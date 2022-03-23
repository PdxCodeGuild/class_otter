print('\nWelcome to the Credit Card Validator!')

#VALID CREDIT CARD NUMBER 4556737586899855

#card_vald = input('\nPlease enter, the sixteen digit credit card number to validate: ')

cred_card_test = '4556737586899855'

def cred_card_vald(card_vald):
    #1.Convert the input string into a list of ints
    list_ints = list(card_vald)
    
    for i in range(len(list_ints)):
        list_ints[i] = int(list_ints[i])
    print(list_ints)
    
    #2.Slice off the last digit. That is the check digit.
    chk_dig = list_ints.pop()
    print(chk_dig)
    
    #3.Reverse the digits
    revrsd_dig = list(reversed(list_ints))
    print(revrsd_dig)
    
    #4.Double every other element in the reversed list (starting with the first number in the list)
    for i in range(0,len(list_ints),2):
         list_ints[i] *= 2
    print(list_ints)
    
    #5.Subtract nine from numbers over nine.
    for i in range(len(list_ints)):
        if list_ints[i] > 9:
            list_ints[i] -= 9
    print(list_ints)

    #6.Sum all values
    sum_list_ints = 0
    for num in list_ints:
        sum_list_ints += num
    print(sum_list_ints)

    #7.Take the second digit of that sum.
    secnd_dig = sum_list_ints % 10
    print(secnd_dig)
    
    #8.If that matches the check digit, the whole card number is valid.
    if secnd_dig == chk_dig:
        print('Credit card is valid!')
    return secnd_dig == chk_dig
    
print(cred_card_vald(cred_card_test))