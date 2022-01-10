# Convert the input string into a list of ints

valid_nums = "4556737586899855"
number = [int(i) for i in valid_nums]

# print(number)


# Slice off the last digit. That is the check digit.
check_digit = number.pop()
# print(check_digit)

# Reverse the digits.
number.reverse()
# print(number)

# Double every other element in the reversed list (starting with the first number in the list).
reversed_list = [(number[i] * 2 if i % 2 == 0 else number[i]) for i in range(len(number))]

# print(reversed_list)
# Subtract nine from numbers over nine.
subtract_list = []

for i in reversed_list:
    if i > 9:
        i -= 9
    subtract_list.append(i)
# print(subtract_list)    

# Sum all values.
sum = 0
for j in subtract_list:
    sum += j
# print(sum)

# Take the second digit of that sum.
second_digit = int(str(sum))
if second_digit[1] == check_digit:
    print("Valid")
else:
    print("Invalid")
# If that matches the check digit, the whole card number is valid.
