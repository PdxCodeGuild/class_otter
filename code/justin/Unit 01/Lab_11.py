# Full Stack Bootcamp - Unit 01 Lab 11
# Justin Hammond, 01/10/2022


'''
Part 1 - Linear Search
Implement linear search, which simply loops through the given list and
check if each element is equal to the value we're searching for. If it is,
return the index at which it was found, otherwise, return a value
indicating that it was not found.

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


Part 2 - Binary Search
Implement binary search, which requires that a list is sorted and divides
its search range in half each iteration until it finds its target.

Begin by defining two indices: low and high. Initialize low as the lowest
index in the list and high as the highest.

Loop while low is less then high.

For each iteration, calculate a third index mid which is in the middle
between low and high

If the element at mid is the one you're searching for, return it,
otherwise check is the target value is less than or greater than the one
at mid.

If it's less, make high equal to mid and loop.

If it's greater, make low equal to mid and loop.

If the loop terminates without returning, return a value indicating that
it was not found.

Example run:
 L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
 L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]

Psuedocode:
// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful

Stub:
def binary_search(nums, value):
  ...
#       0  1  2  3  4  5  6  7
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = linear_search(nums, 3)
print(index) # 2
'''
import math


def linear_search(nums, value):
    for i in range(len(nums)):
        if nums[i] == value:
            return i
        
    return -1

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8], 20) == -1

def binary_search(nums, value):
    low = 0
    high = len(nums) - 1
    mid = 0
    num = 0
    while low <= high:
        mid = math.floor((low + high) / 2)
        num = nums[mid]
        if num == value:
            return mid
        elif num < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 20) == -1


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    index = linear_search(nums, 3)
    print(index)

    nums.sort()
    index = binary_search(nums, 3)
    print(index)


main()