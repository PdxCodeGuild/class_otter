# Full Stack Bootcamp - Unit 01 Practice 06
# Justin Hammond, 01/05/2022


# Create Contact ===============================================================
# Write a function that returns a dictionary representing a contact given their name and age.

def create_contact(name, age):
    return dict({'name': name, 'age': age})

def test_create_contact():
    assert create_contact('Bob', 67) == {'name': 'Bob', 'age': 67}
    assert create_contact('Linda', 34) == {'name': 'Linda', 'age': 34}

# print(create_contact('Bob', 67))  # {'name': 'Bob', 'age': 67}
# print(create_contact('Linda', 34)) # {'name': 'Linda', 'age': 34}


# Has Key ======================================================================
# Write a function that returns `True` if the given dictionary has the given key, `False` otherwise.

def has_key(d, key):
    return key in d

def test_has_key():
    assert has_key({'a': 1, 'b': 2}, 'a') == True
    assert has_key({'a': 1, 'b': 2}, 'c') == False

# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False


# Is Empty =====================================================================
# Write a function that returns `True` if the given dictionary is empty, `False` otherwise.

def is_empty(d):
    return len(d) == 0

def test_is_empty():
    assert is_empty({}) == True
    assert is_empty({'a': 1, 'b': 2}) == False

# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False


# Find Key =====================================================================
# Write a function that finds and returns the **key** for the given **value**, if the value is not in the dictionary, it should return `None`.

def find_key(d, value):
    for item in d.items():
        if item[1] == value:
            return item[0]

    return None

def test_find_key():
    assert find_key({'a': 1, 'b': 2}, 1) == 'a'
    assert find_key({'a': 1, 'b': 2}, 3) == None

# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None


# Reverse Dict =================================================================
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

def reverse_dict(d):
    result = {}
    for item in d.items():
        result[item[1]] = item[0]

    return result

def test_reverse_dict():
    assert reverse_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}

# print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}


# Merge ========================================================================
# Write a function that mergest two lists of equal length into a dictionary, with the first list containing the keys, and the second containing the values.

def merge(list1, list2):
    result = {}
    for index in range(len(list1)):
        result[list1[index]] = list2[index]

    return result

def test_merge():
    assert merge(['a', 'b'], [1, 2]) == {'a': 1, 'b': 2}

# print(merge(['a', 'b'], [1, 2])) # {'a': 1, 'b': 2}


# Remove Less Than 10 =========================================================
# Write a function that takes a dictionary and returns a new dictionary without values less than 10.

def remove_less_than_10(d):
    result = {}
    for item in d.items():
        if item[1] >= 10:
            result[item[0]] = item[1]

    return result

def test_remove_less_than_10():
    assert remove_less_than_10({'a': 5, 'b': 15, 'c': 12}) == {'b': 15, 'c': 12}

# print(remove_less_than_10({'a': 5, 'b': 15, 'c': 12})) # {'b': 15, 'c': 12}


# Average ======================================================================
# Write a function to calculate the average of the lists in a dictionary.

def average_values(d):
    result = {}
    sum = 0
    for item in d.items():
        sum = 0
        for value in item[1]:
            sum += value
        result[item[0]] = sum / len(item[1])
    
    return result

def test_average_values():
    assert average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]}) == {'a': 4, 'b': 5, 'c': 3}
# print(average_values({'a': [1, 5, 6], 'b': [2, 8], 'c': [3]})) # {'a': 4, 'b': 5, 'c': 3}


# Merge Dictionaries ===========================================================
# Write a function that takes two dictionaries and returns a new dictionary with the values from each added together if they have the same key

def merge_dictionaries(d1, d2):
    result = {}
    for item in d1.items():
        key = item[0]
        if key in result:
            result[key] += item[1]
        else:
            result[key] = item[1]

    for item in d2.items():
        key = item[0]
        if key in result:
            result[key] += item[1]
        else:
            result[key] = item[1]

    return result

def test_merge_dictionaries():
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}
    assert merge_dictionaries(d1, d2) == {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# print(merge_dictionaries(d1, d2)) # {'a': 400, 'b': 400, 'c': 300, 'd': 400}


# Count Votes ==================================================================
# Write a function that takes a list of strings and counts of the number of occurances.

def count_votes(votes):
    result = {}
    for vote in votes:
        if vote in result:
            result[vote] += 1
        else:
            result[vote] = 1
    
    return result

def test_count_votes():
    votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
    assert count_votes(votes) == {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}

# votes = ['john', 'johnny', 'john', 'jackie', 'jamie', 'jackie', 'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
# print(count_votes(votes)) # {'john': 4, 'johnny': 3, 'jackie': 2, 'jamie': 4}


# Problem 6 ====================================================================
# Write a function `cart_total` to calculate the total of a shopping cart given a list of dictionaries representing a cart and a dictionary representing prices.

def cart_total(prices, cart):
    result = 0
    for item in cart:
        result += prices[item['item']] * item['quantity']

    return result

def test_cart_total():
    prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
    cart = [{'item': 'apples', 'quantity': 3}, {'item': 'kiwis', 'quantity': 4}]
    assert cart_total(prices, cart) == 11.0

# prices = {'apples': 1.0, 'bananas': 0.5, 'kiwis': 2.0}
# cart = [{'item': 'apples', 'quantity': 3}, {'item': 'kiwis', 'quantity': 4}]
# print(cart_total(prices, cart)) # 11.0
