cc = '4556737586899855'
import string
def convert(card):
    clist = []
    clist = list(cc)
    return clist
card = convert(cc)
print(card)
#convert string of credit card into a list
card_check = card.copy()
#copied the list for last step of checking the check number & computed credit card info
c_card = []
def slice_check_digit(card):
    num = len(card)
    c_card = card[:(num - 1):]
    return c_card
c_card = slice_check_digit(card)
# print(len(cc))
print(c_card)
# sliced the last number so now the length is 15 versus 16
def reverse(clist):
    card_list = clist[::-1]
    return card_list
cardl = reverse(c_card)
print(cardl)
# reversed the credit card number
nlist = []
def double_element(cc):
    for x in range(len(cc)):
        if x%2 == 0:
            nvalue = int(cc[x]) * 2
        # print(nvalue)
            nlist.append(nvalue)
        # print(nlist)
        if x%2 == 1:
            nlist.append(cc[x])
dcard = double_element(cardl)
print(nlist)
# by deteremining whether x is even or odd I can determined to double or not ie everyother
dlist = []
def subtract_nine(card):
    for x in range(len(card)):
        if int(card[x]) > 9:
            svalue = int(card[x]) - 9
            dlist.append(svalue)
        elif int(card[x]) <= 9:
            svalue = int(card[x])
            dlist.append(svalue)
    return dlist
slist = subtract_nine(nlist)
print(slist)
# print(len(slist))
ulist = []
def sum(ulist):
    main = 0
    for position in range(len(ulist)):
        main = main + ulist[position]
    return main
result = sum(slist)
print(result)
match = result%10
print(match)
# print(card_check)
ccheck = len(card_check)
# print(ccheck)
checkfinal = card_check[int(ccheck) - 1]
# print(checkfinal)
if int(match) == int(checkfinal):
    print("Valid!")
else:
    print("not Valid...")