



def is_even(a):
    return a % 2 ==0

def test_is_even():
    assert is_even(5) == False
    assert is_even(6) == True


def ones_digit(num):
    return num % 10

def test_ones_digit():
    assert ones_digit(3) == 3
    assert ones_digit(56) == 6
    assert ones_digit(812) == 2
