# Full Stack Bootcamp - Unit 01 Lab 02
# Justin Hammond, 01/05/2022


# We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum',
# then divide that sum by the number of elements in that list. Remember len will give you the length of a list.
# nums = [5, 0, 8, 3, 4, 1, 6]

def average_list_v1(list):
    sum = 0

    for item in list:
        sum += item

    return sum / len(list)

def test_average_list_v1():
    assert average_list_v1([5, 0, 8, 3, 4, 1, 6]) == 3.857142857142857
