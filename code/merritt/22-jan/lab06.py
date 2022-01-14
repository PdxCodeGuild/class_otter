def credit_card_validator(original_number):
    list_of_ints = [int(num) for num in original_number]
    check_digit = list_of_ints.pop()
    reversed_digits = list(reversed(list_of_ints))
    every_other_doubled = [digit * 2 if i % 2 == 0 else digit for i, digit in enumerate(reversed_digits)]
    # every_other_doubled = [reversed_digits[i] * 2 if i % 2 == 0 else reversed_digits[i] for i in range(len(reversed_digits))]
    subtract_nine = [digit - 9 if digit > 9 else digit for digit in every_other_doubled]
    digit_sum = sum(subtract_nine)
    second_digit = digit_sum % 10
    return second_digit == check_digit

    # list_of_ints = list(original_number)
    # for i in range(len(list_of_ints)):
    #     list_of_ints[i] = int(list_of_ints[i])
    # # list2 = []
    # # for char in list_of_ints:
    # #     list2.append(int(char))

    # check_digit = list_of_ints.pop()

    # list_of_ints.reverse()

    # for i in range(0, len(list_of_ints), 2):
    #     list_of_ints[i] *= 2

    # for i in range(len(list_of_ints)):
    #     if list_of_ints[i] > 9:
    #         list_of_ints[i] -= 9

    # # list_of_ints_sum = 0
    # # for num in list_of_ints:
    # #     list_of_ints_sum += num

    # list_of_ints_sum = sum(list_of_ints)

    # second_digit = list_of_ints_sum % 10


    # print(orginal_number)
    # print(list_of_ints)
    # print(list_of_ints_sum)
    # print(second_digit)
    # print(check_digit)

    # return second_digit == check_digit




print(credit_card_validator("4556737586899855"))