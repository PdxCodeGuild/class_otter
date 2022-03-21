# Full Stack Bootcamp - Unit 01 Practice 05
# Justin Hammond, 01/04/2022


# Practice 5: Lists
# Copy and paste this file into your own "05_lists.py"
# Fill in the code for each of the functions
# Run the tests by typing "pytest 05_lists.py"


# Even Even
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def is_even(num):
    return num%2 == 0

def even_even(nums):
    even_count = 0
    for num in nums:
        even_count += 1 if is_even(num) else 0
    return is_even(even_count)

def test_even_even():
    assert even_even([5, 6, 2]) == True
    assert even_even([5, 5, 2]) == False


## Reverse
# Write a function that takes a list and returns a new list with the elements in reverse order

def reverse(nums):
    result = []
    
    i = len(nums) - 1
    while i >= 0:
        result.append(nums[i])
        i -= 1

    return result

def test_reverse():
    assert reverse([1, 2, 3]) == [3, 2, 1]


# Common Elements
# Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
    result = []
    for num in nums1:
        if num in nums2:
            result.append(num)
    return result

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


# Combine
# Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):
    results = []
    for i in range(len(nums1)):
        results.append(nums1[i])
        results.append(nums2[i])
    return results

def test_combine():
    assert combine(['a','b','c'],[1,2,3]) == ['a', 1, 'b', 2, 'c', 3]


# Find Pair
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.

def find_pair(nums, target):
    nums.sort()
    pairs = []
    temp_nums = nums
    for i in range(len(nums)):
        other_target = target - temp_nums.pop(0)
        for other_num in temp_nums:
            if other_num == other_target:
                pairs.append([target - other_num, other_num])
    return pairs


def test_find_pair():
    pairs = find_pair([5, 6, 2, 3], 7)
    
    assert len(pairs) == 1
    assert pairs[0] == [2, 5]

    pairs = find_pair([5, 6, 2, 3, 4], 7)
    assert len(pairs) == 2
    assert pairs[0] == [2, 5]
    assert pairs[1] == [3, 4]


# Average
# Write a function to find the average of a list of numbers

def average(nums):
    sum = 0
    count = len(nums)
    if count == 0:
        return 0
        
    for num in nums:
        sum += num
    return sum / len(nums)

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([-6, 37, 2, 0, 0, 1]) == 5 + (2 / 3)


# Remove Empty
# Write a function to remove all empty strings from a list.

def remove_empty(mylist):
    result = []
    for element in mylist:
        if len(element) > 0:
            result.append(element)
    return result

def test_remove_empty():
    assert remove_empty(['a', 'b', '', 'c', '', 'd']) == ['a', 'b', 'c', 'd']



# Merge
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

def merge(nums1, nums2):
    result = []
    for index in range(len(nums1)):
        result.append([nums1[index], nums2[index]])
    return result

def test_merge():
    assert merge([5,2,1], [6,8,2]) == [[5,6],[2,8],[1,2]]


# Combine All
# Write a function `combine_all` that takes a list of lists, and returns a list containing each element from each of the lists.

def combine_all(nums):
    result = []
    for list in nums:
        for num in list:
            result.append(num)
    return result

def test_combine_all():
    assert combine_all([[5,2,3],[4,5,1],[7,6,3]]) == [5,2,3,4,5,1,7,6,3]


# Fibonacci
# Write a function that takes `n` as a parameter, and returns a list containing the first `n` [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number).

def fibonacci(n):
    result = []
    i = 0
    j = 1
    fibonacci_number = 0
    count = 0
    while count < n:
        count += 1
        i = j
        j = fibonacci_number
        fibonacci_number = i + j

        result.append(fibonacci_number)
    return result

def test_fibonacci():
    assert fibonacci(8) == [1, 1, 2, 3, 5, 8, 13, 21]

# Factorial
# Write a function that takes `n` as a parameter and returns `n` factorial.

def factorial(n):
    result = 1
    for i in range(n):
        result *= i + 1
    return result

def test_factorial():
    assert factorial(5) == 120


# Find Unique
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.

def find_unique(nums):
    uniques = {}
    for num in nums:
        uniques[num] = True

    result = []
    for unique_num in uniques:
        result.append(unique_num)
    return result

def test_find_unique():
    nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    assert find_unique(nums) == [12, 24, 35, 88, 120, 155]
