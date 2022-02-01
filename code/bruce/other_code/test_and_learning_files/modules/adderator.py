def add_two_things(thing_01, thing_02):
    '''Adds two arguments together. Returns result of concatenation of strings
    or numeric addition.
    '''
    return thing_01 + thing_02

# print(add_two_things(3,4))
# print(add_two_things('a','b'))

def test_add_two_things():
    assert add_two_things(3, 4) == 7
    assert add_two_things('a','b') == 'ab'
    one_thing = 7
    another_thing = 8
    assert add_two_things(one_thing, another_thing) == 15

