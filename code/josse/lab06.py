# convert string into interger

user = input("please enter your number:  ")


def validator(credit_card_number):
    list_ints = []

    # convert string to list:
    for i in (credit_card_number):
        list_ints.append(int(i))

    # removes last digit:
    check_digit = list_ints.pop()

    # reverses digits:
    list_ints.reverse()

    # double every other digit starting with the first number:
    for i in range(len(list_ints)):
        if i % 2 == 0:
            list_ints[i] = list_ints[i] * 2

    # subtract 9 from numbers over 9
    for i in range(len(list_ints)):
        if list_ints[i] > 9:
            list_ints[i] = list_ints[i] - 9

    # sum all values
    total = 0
    for i in list_ints:
        total += i

    # take second digit of sum:
    string_total = str(total)

    second_digit = string_total[-1]

    if int(second_digit) == check_digit:
        return "Valid!"
    else:
        return "Not Valid!"


print(validator(user))
# def double_every_other(list_ints):
#     for i in range(len(list_ints)):
#         if (i % 2) == 0:
#             list_ints[i] = list_ints[i] * 2
#     return list_ints


# def subtract_nine(list_ints):
#     for number in (list_ints):
#         if number > 9:
#             del number[list_ints]
#     return list_ints


# print(validator(user))


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
