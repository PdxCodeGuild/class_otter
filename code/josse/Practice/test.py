def ones_digit(num):
    if len(str(num)) == 1:
        result = num
    if len(str(num)) > 1:
        num_as_string = str(num)
        num_as_string[len(num_as_string) -1]
        result = num
    return result
    
num_as_string = "256"

print(f'''
number {num_as_string} 
length {len(num_as_string)}
first number {num_as_string[0]} {0}
second number {num_as_string[1]} {1}
third number {num_as_string[len(num_as_string)-1]} {len(num_as_string)-1}
''')