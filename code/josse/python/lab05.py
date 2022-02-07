import random


def six_numbers():
    nums = []
    for i in range(6):
        nums.append(random.randint(1, 99))
        return nums


print(six_numbers)
