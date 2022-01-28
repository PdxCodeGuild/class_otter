# convert string into interger
user = input("please enter your number:  ")


def main(credit_card_number):
    list_ints = []
    for i in (credit_card_number):
        list_ints.append(int(i))
    check_digit = list_ints.pop()
    list_ints.reverse()
    for numbers in list_ints:
        numbers * 2
        print(numbers)


main(user)

# def remove_last_digit(credit_card_number):
#     for i in list_ints:
#     new_list = []
#         i[list_ints].remove(-1)
#         new_list.append(i)
#     return new_list


# print(type(main(user)))


# return (i)
# print(type(i))
# i += 1
# credit_card_number.pop(-1)
# print(credit_card_number)
# print(main(user))
#  4556737586899855
# print(main(type(user))
