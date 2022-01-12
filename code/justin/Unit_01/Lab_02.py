# Full Stack Bootcamp - Unit 01 Lab 02
# Justin Hammond, 01/05/2022


# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum',
# then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
# nums = [5, 0, 8, 3, 4, 1, 6]

def average_list(list):
    sum = 0

    for item in list:
        sum += item

    return sum / len(list)

def test_average_list():
    assert average_list([5, 0, 8, 3, 4, 1, 6]) == 3.857142857142857



def is_done(response):

    return str(response).lower() == 'done'

def test_is_done():
    assert is_done(5) == False
    assert is_done('d') == False
    assert is_done('done') == True
    assert is_done('DoNe') == True
    assert is_done('DONE') == True

def get_list_from_user():
    result = []
    response = ""
    while not is_done(response):
        if len(response) != 0:
            result.append(int(response))
        response = input("Enter a number, or [done]: ")

    return result

def display_list_average():
    list_to_average = get_list_from_user()
    average = average_list(list_to_average)

    print(average)

display_list_average()