# convert string into interger
user = input("please enter your number:  ")


def validator(credit_card_number):
    list_ints = []
    for i in (credit_card_number):
        list_ints.append(int(i))
    check_digit = list_ints.pop()
    list_ints.reverse()
    list_ints = double_every_other(list_ints)

    return list_ints


def double_every_other(list_ints):
    for i in range(len(list_ints)):
        if (i % 2) == 0:
            list_ints[i] = list_ints[i] * 2
    return list_ints


print(validator(user))


# print(double_every_other([1, 2, 3, 4]))
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
