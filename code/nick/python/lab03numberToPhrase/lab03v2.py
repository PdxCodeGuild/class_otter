user_input = int(input('enter a number. '))

hundreds_digit = user_input // 100
tens_digit = (user_input // 10)% 10
ones_digit = user_input % 10
print(hundreds_digit,',', tens_digit,',',ones_digit)

ones_place = {
0: 'zero',
1: 'one', 2 : 'two', 3 : 'three', 4: 'four', 5: 'five', 6: 'six',
7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

tens_place = {
2: 'twenty', 3: 'thirty', 4: 'fourty', 5:'fiftey', 6: 'sixtey', 
7: 'seventy', 8: 'eighty', 9: 'ninety'}

teens = {1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}

if user_input <20:
    print(ones_place[user_input])

if 100> user_input >= 20:
    
    if ones_digit == 0:
        print(tens_place[tens_digit])
    else:
        print(tens_place[tens_digit], ones_place[ones_digit])

elif 1000 > user_input:
    if ones_digit == 0 and tens_digit == 0:
        print(ones_place[hundreds_digit],'hundred')
    elif tens_digit == 0:
        print(ones_place[hundreds_digit], 'hundred', ones_place[ones_digit])
    elif ones_digit == 0:
        print(ones_place[hundreds_digit], 'hundred', tens_place[tens_digit])
    if tens_digit > 1:
        print(ones_place[hundreds_digit], 'hundred', tens_place[tens_digit], ones_place[ones_digit])
    elif tens_digit == 1:
        print(ones_place[hundreds_digit], 'hundred', teens[ones_digit] )
