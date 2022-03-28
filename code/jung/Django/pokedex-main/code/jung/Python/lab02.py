nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
# for num in nums:
#     print(num)

# loop over the indices
# for i in range(len(nums)):
#     print(nums[i])

#Version 2


nums = []

true_or_false = True
while true_or_false:
    answer = input("enter a number, or 'done': ")
    if answer != "done":
        answer = int(answer)
        nums.append(answer)
    elif answer == "done":
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            true_or_false = False
            average = add / len(nums)
        print(f"average: {average}")