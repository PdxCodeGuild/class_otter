import random
import string
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
all_characters = letters + digits + punctuation
password = []
print ("This is the 'Password Generator'")

while len(password) < 10:
    #add a random character to the list
    password.append(random.choice(all_characters))
def listToString(password):
    str1 = ""
    return (str1.join(password))
print("\nHere is your Random Password:\n")
print(listToString(password))

# number = input('''please enter the number of 
# password characters between 8 and 16:''')