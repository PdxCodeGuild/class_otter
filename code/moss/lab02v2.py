user_num_list = []

answer = 0

while True:

    user_num = input("\nWelcome to the averaging tool, enter your number or 'done' to quit:\n")

    if user_num == 'done':

        answer = sum (user_num_list)/len(user_num_list)

        print(f'The average is : {answer}')

        break
    
    else :
        
        user_num = int(user_num)

        user_num_list.append(user_num)
