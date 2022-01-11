# Full Stack Bootcamp - Unit 01 Practice 07
# Justin Hammond, 01/05/2022


# Practice 6: Regular Expressions
import re


# Validate an Email Address
# Write a function `validate_email_address` which returns `True` if the given string is an email address, `False` is it isn't.

def validate_email_address(email):
    pattern = r"[^\s@]+@[^\s@]+\.[^\s@]+"
    return re.match(pattern, email) != None

def test_validate_email_address():
    assert validate_email_address('test@gmail.com') == True
    assert validate_email_address('abc123@gmail.com') == True
    assert validate_email_address('test') == False
    assert validate_email_address('test@gmail') == False
    assert validate_email_address('test@gmail@com') == False

# print(validate_email_address('test@gmail.com')) # True
# print(validate_email_address('abc123@gmail.com')) # True
# print(validate_email_address('test')) # False
# print(validate_email_address('test@gmail')) # False
# print(validate_email_address('test@gmail@com')) # False


# Validate a Phone Number
# Write a function `validate_phone_number` which returns `True` if the given string is a phone number, `False` if it isn't.

# https://regex101.com/r/lCV6nR/1
def validate_phone_number(phone_number):
    pattern = r"^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}"
    return re.match(pattern, phone_number) != None

def test_validate_phone_number():
    assert validate_phone_number('0123456789') == True
    assert validate_phone_number('012-345-6789') == True
    assert validate_phone_number('(012) 345-6789') == True
    assert validate_phone_number('012-3A5-6789') == False
    assert validate_phone_number('1-1-1') == False

# print(validate_phone_number('0123456789')) # True
# print(validate_phone_number('012-345-6789')) # True
# print(validate_phone_number('(012) 345-6789')) # True
# print(validate_phone_number('012-3A5-6789')) # False
# print(validate_phone_number('1-1-1')) # False


# Clean a Phone Number
# Write a function `clean_phone_number` which returns a string containing just the numbers of a phone number if it's valid, `None` if it's not. Hint: use capture groups.

def clean_phone_number(phone_number):
    pattern = r"^\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{4})"
    match_result = re.match(pattern, phone_number)
    if match_result == None:
        return None
    else:
        return f"{match_result.group(1)}{match_result.group(2)}{match_result.group(3)}"

def test_clean_phone_number():
    assert clean_phone_number('0123456789') == '0123456789'
    assert clean_phone_number('012-345-6789') == '0123456789'
    assert clean_phone_number('(012) 345-6789') == '0123456789'
    assert clean_phone_number('012-3A5-6789') == None
    assert clean_phone_number('1-1-1') == None

# print(clean_phone_number('0123456789')) # 0123456789
# print(clean_phone_number('012-345-6789')) # 0123456789
# print(clean_phone_number('(012) 345-6789')) # 0123456789
# print(clean_phone_number('012-3A5-6789')) # None
# print(clean_phone_number('1-1-1')) # None


# Find All Numbers
# Write a function `find_numbers` which returns a list of floats found in the given string.

def find_numbers(text):
    pattern = r"[-?\d][.\d]+"
    match_results = re.findall(pattern, text)
    results = []
    for value in match_results:
        results.append(float(value))

    return results

def test_find_numbers():
    text = '''
    name  favorite number
    joe   1.23
    jane  5.45
    julie -1.34
    bob   43.123
    '''
    assert find_numbers(text) == [1.23, 5.45, -1.34, 43.123]

# print(find_numbers(text)) # [1.23, 5.45, -1.34, 43.123]
