print('\nWelcome to ROT Cipher!\n')

usr_string = input('Enter a string to encode:') # Asks user

usr_string_list= list(usr_string) #Turns user input into list
output_list = [] # Empty list container

eng_to_rot = {'a':'n','b':'o','c':'p','d':'q','e':'r', 'f':'s', 
'g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','o':'b', 
'l':'y','m':'z','o':'b', 'p':'c','q':'d','r':'e','s':'f','t':'g',
'u':'h','v':'i','w':'j','x':'k','y':'l','z':'m', ' ':' '} 
# Added empty string ' ' : ' ' key:value

for letter in usr_string_list:
    output_list.append(eng_to_rot[letter]) 
#Loops each letter list, cycles dictionary to match letter to keys->
#->to be added to empty list container

output_string = ''.join(output_list)
#.join combines the elements of a list into a single string

print(output_string)
