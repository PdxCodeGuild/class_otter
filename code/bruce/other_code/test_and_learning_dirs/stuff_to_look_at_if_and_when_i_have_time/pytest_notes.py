# Is the order of these a style recommendation?
# def functions() >> def main() >> def test_functions()

def do_cool_stuff(value):
    return value * value

def square_number(number_to_be_squared=0):
    return number_to_be_squared ** 2
	
def main():
    user_provided_value = input("Gimme something: ")
    print(user_provided_value)

    num_to_square = 5
    squared_num = square_number(num_to_square)
    print(f'{num_to_square} squared is {squared_num}')

def test_square_number():
    assert square_number() == 0
    assert square_number(2) == 4
    assert square_number(9) == 81


def test_do_cool_stuff():
    assert do_cool_stuff(1) == 1
    assert do_cool_stuff(-1) == 1
    assert do_cool_stuff(6) == 36

# To make testing easier, wrap the calling of main() in an if statement as shown here.
if __name__ == '__main__':
    main()