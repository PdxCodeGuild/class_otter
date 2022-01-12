"""
Lab 3: Number to Phrase

"""

"""
Version 1

"""

print()

single = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
odds = {10: 'ten', 11: 'eleven', 12: 'twelve'}

number = int(input("Enter a number: "))

tens_digit = number // 10
ones_digit = number % 10

for num in single:
    if num == number:
        print(single[number])
        break
for num in odds:
    if num == number:
        print(odds[number])
        break
for num in teens:
    if num == number:
        print(teens[number])
        break
for num in tens:
    if num == tens_digit and ones_digit == 0:
        print(tens[tens_digit])
        break
    elif num == tens_digit:
        
        for num in single:
            print(tens[tens_digit]+ ' ' + single[ones_digit])
            break


'''
Version 2
'''


hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred',
5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred',
9: 'nine hundred'}

hundred_digit = number // 100
hundred_tens_digit = ((number % 100) // 10)
hundred_single_digit = (number % 10)
hundred_odds_check = number % 100


for num in hundreds:
    
    if number == 100:
        print(hundreds[hundred_digit])
        break

    elif num == hundred_digit:

        for num in tens:

            if hundred_tens_digit == 0:

                print(hundreds[hundred_digit] + ' ' + single[hundred_single_digit])
                break


for num in hundreds:

    if hundred_odds_check >= 10 and hundred_odds_check <= 12 and number > 99:
        
        print(hundreds[hundred_digit] + ' ' + odds[hundred_odds_check])
        break

for num in hundreds:

    if hundred_odds_check >= 13 and hundred_odds_check <= 19 and number > 99:
        print(hundreds[hundred_digit] + ' ' + teens[hundred_odds_check])
        break        


for num in hundreds:
    
    if num == hundred_digit:
        
        for num2 in tens:
            
            if num2 == hundred_tens_digit:
                
                for num3 in single:
                    
                   
                    if hundred_digit > 0 and hundred_tens_digit > 0 and hundred_single_digit == 0:
                        print(hundreds[hundred_digit] + ' ' + tens[hundred_tens_digit])
                        break
                    elif hundred_tens_digit > 0:
                        print(hundreds[hundred_digit] + ' ' + tens[hundred_tens_digit]+ ' ' + single[hundred_single_digit]) 
                        break    
print()