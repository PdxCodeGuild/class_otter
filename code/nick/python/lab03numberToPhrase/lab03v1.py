x = int(input('enter a number. '))

hundreds_digit = x // 100
tens_digit = x // 10
ones_digit = x % 10

number_words_1 = [
    'zero' , 'one', 'two', 'three', 'four', 'five', 
'six', 'seven', 'eight', 'nine', 'ten', 
'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen'
]

ones_place = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


if x <= 19:
    print(number_words_1[x])
elif 2 <= tens_digit < 3:
    print('twenty', ones_place[ones_digit])
elif 3 <= tens_digit < 4:
    print('thirty',ones_place[ones_digit])
elif 4 <= tens_digit <5:
    print('fourty', ones_place[ones_digit])
elif 5 <= tens_digit <6:
    print('fiftey', ones_place[ones_digit])
elif 6 <= tens_digit <7:
    print('sixty', ones_place[ones_digit])
elif 7 <= tens_digit <8:
    print('seventy', ones_place[ones_digit])
elif 8 <= tens_digit <9:
    print('eighty' , ones_place[ones_digit])
elif 9 <= tens_digit <10:
    print('ninety', ones_place[ones_digit])
