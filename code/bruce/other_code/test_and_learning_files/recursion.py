# ********************************** #
#            Recursion!!!            #
#   Using a function within itself   #
#            Version: 0.0            #
#        Author: Bruce Stull         #
#             2022-01-17             #
# ********************************** #

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/10%20Functions.md

from unittest import result


def factorial(n = 0):
    if n == 0:
        return 1
    return n*factorial(n-1)

def test_factorial():
    assert factorial() == 1
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6

# Try making fibonacci function.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610
def fibonacci(n = 1):
    '''Returns the nth fibonacci number.'''
    if n == 1:
        result = 1
    elif n == 2:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    return result

def test_fibonacci():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(11) == 89

# 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibonacci_sequence(n = 1):
    '''Returns fibonacci sequence of n elements as a list.'''
    # How to append fib(1) then fib(2) etc?
    # range(4) 0, 1, 2, 3 ==> 1, 2, 3, 4
    # range(3) 0, 1, 2 ==> 1, 2, 3
    # range(2) 0, 1 ==> 1, 2

    fibonacci_list = []
    for index in range(1, n + 1):
        fibonacci_list.append(fibonacci(index))
    return fibonacci_list

def test_fibonacci_sequence():
    assert fibonacci_sequence(1) == [1]
    assert fibonacci_sequence(2) == [1,1]
    assert fibonacci_sequence(3) == [1,1,2]
    assert fibonacci_sequence(4) == [1,1,2,3]
    assert fibonacci_sequence(9) == [1,1,2,3,5,8,13,21,34]

# for i in range(5):
#     print(i)
# # 0
# # 1
# # 2
# # 3
# # 4

# fibonacci_list = []

# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))

# print(fibonacci_list)
# fibonacci_list.append(fibonacci(1))
# fibonacci_list.append(fibonacci(2))
# fibonacci_list.append(fibonacci(3))
# fibonacci_list.append(fibonacci(4))
# print(fibonacci_list)
