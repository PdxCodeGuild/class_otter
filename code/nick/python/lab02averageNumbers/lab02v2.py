nums = []


while True:
    user_input = input("enter a number or 'done': ")
    if user_input == 'done':
        break
    nums.append(int(user_input))
print( f'average: {sum(nums)/len(nums)}')
