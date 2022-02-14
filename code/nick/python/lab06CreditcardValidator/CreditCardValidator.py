def credit_card_validator(original_numbers):
    num_list = list(original_numbers)
    for i in range(0, len(num_list)):
        num_list[i] = int(num_list[i])
    check_digit = num_list.pop()
    num_list.reverse()
    for i in range(0, len(num_list),2):
        num_list[i] *=2 
    for i in range(len(num_list)):
        if num_list[i]>9:
            num_list[i]-=9
    sum_list = sum(num_list)
    digits = [int(x) for x in str(sum_list)]
    if digits[1] == check_digit:
        return True


print(credit_card_validator("4556737586899855"))
