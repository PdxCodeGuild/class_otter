def credit_card_validator(original_number):
    list_of_ints = [int(num) for num in original_number]
    check_digit = list_of_ints.pop()
    reversed_digits = list(reversed(list_of_ints))
    every_other_doubled = [digit * 2 if i % 2 == 0 else digit for i, digit in enumerate(reversed_digits)]
    subtract_nine = [digit - 9 if digit > 9 else digit for digit in every_other_doubled]
    digit_sum = sum(subtract_nine)
    second_digit = digit_sum % 10
    return second_digit == check_digit



print(credit_card_validator("4556737586899855"))
