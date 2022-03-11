'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*             Lab 07 - ROT13                *
*            10/January/2022                *
*                                           *
*********************************************
'''

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

