#Lab07.py "ROT Cipher" - 22-01-10 - Scott Madden
import string
def rot13(ciph): #Define rot13(ciph) function
   abc = string.ascii_letters
#    print(abc)
   output_cipher = ""
   for char in ciph:
       output_cipher += abc[(abc.find(char)+13)%26]
   return output_cipher

ciph = input("Please enter some letters:")
print(rot13(ciph))
print(rot13(rot13(ciph)))

