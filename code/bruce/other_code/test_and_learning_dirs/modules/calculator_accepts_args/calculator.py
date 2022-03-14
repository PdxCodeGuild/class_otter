
# Fibonacci numbers module

# Print Fibonacci series up to n.
def fib_print_n(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# return Fibonacci series up to n.
def fib_return_n_list(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    import sys
    fib_print_n(int(sys.argv[1]))
    nums_list = fib_return_n_list(int(sys.argv[2]))
    for num in nums_list:
        print(num)
    print(sys.argv[1])
    print(sys.argv[2])