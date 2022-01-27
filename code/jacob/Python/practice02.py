"""
Practice 02
Booleans, Dictionaries

"""

def go_hiking(energy, weather):
    if energy == 'spry' and weather == 'sunny':
        return True

    else:
        return False

def test_go_hiking():
    assert go_hiking('tired', 'rainy') == False
    assert go_hiking('tired', 'sunny') == False
    assert go_hiking('spry', 'rainy') == False
    assert go_hiking('spry', 'sunny') == True

#print(go_hiking('spry', 'rainy')) == False
#print(go_hiking('spry', 'sunny')) == True

def double_digit(num):
    x = abs(num // 10)
    if x > 0 and x < 10:
        return True

    else:
        return False


def test_double_digit():
    assert double_digit(5) == False
    assert double_digit(55) == True
    assert double_digit(672) == False
    assert double_digit(-56) == True

#print(double_digit(5)) == False
#print(double_digit(56)) == True
#print(double_digit(673)) == False

def opposite(a, b):
    return a * b < 0

def test_opposite():
    assert opposite(10, -1) == True
    assert opposite(2, 3) == False
    assert opposite(-1, -1) == False
    assert opposite(-1, 1) == True

#print(opposite(2, -4)) == True
#print(opposite(2, 4)) == False

def near_100(num):
    if num <= 110 and num >= 90:
        return True

    else:
        return False    

def test_near_100():
    assert near_100(50) == False
    assert near_100(99) == True
    assert near_100(105) == True
    assert near_100(115) == False

# print(near_100(99)) == True
# print(near_100(101)) == True
# print(near_100(87)) == False
# print(near_100(111)) == False

def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a

    elif b > a and b > c:
        return b

    elif c > a and c > b:
        return c
    
    else:
        return 'They are the same.' 

def test_maximum_of_three():
    assert maximum_of_three(5,6,2) == 6
    assert maximum_of_three(-4,3,10) == 10

# print(maximum_of_three(3, 5, 7)) == 7
# print(maximum_of_three(9, 5, 3)) == 9 
# print(maximum_of_three(1, 9, 5)) == 9 
# print(maximum_of_three(9, 9, 9)) == They are the same.

def new_contact(name, age):
    contact = {'name': name, 'age': age}
    
    return contact


# print(new_contact('joe', 15)) == {'name': 'joe', 'age': 15}
# print(new_contact('sue', 17)) == {'name': 'sue', 'age': 17}
# print(new_contact('john', 16)) == {'name': 'john', 'age': 16}

def has_key(d, key):
    for i in d:
        if i == key:
            return True
        else:
            return False

# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False

def is_empty(d):
    if len(d) == 0:
        return True
    else:
        return False    
# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False

def find_key(d, value):
    for i in d:
        if d[i] == value:
            return i

# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None

def reverse_dict(d):
    x = {}
    for i in d:
        x[d[i]] = i          
    return x
# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}

def merge(list1, list2):
    x = {}
    for i in range(len(list1)):
        x.update({list1[i]: list2[i]})
    return x
# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}

def remove_less_than_10(d):
    x = {}
    for i in d:
        if d[i] >= 10:
            x[i] = d[i]
    return x
# print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12, 'd': 7})) # {'b': 15, 'c': 12}

