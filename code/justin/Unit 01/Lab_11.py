# Full Stack Bootcamp - Unit 01 Lab 11
# Justin Hammond, 01/10/2022


'''
Part 1 - Linear Search
Implement linear search, which simply loops through the given list and check if each element is equal
to the value we're searching for. If it is, return the index at which it was found, otherwise, return
a value indicating that it was not found.

Example run:
 I
[1, 2, 3, 4, 5, 6, 7, 8]
    I
[1, 2, 3, 4, 5, 6, 7, 8]
       I
[1, 2, 3, 4, 5, 6, 7, 8]

Stub:
def linear_search(nums, value):
  ...
# index 0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
'''

def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
        
    return -1

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8], 20) == -1


def main():
    nums = range(1, 9)
    index = linear_search(nums, 3)
    print(index)


main()