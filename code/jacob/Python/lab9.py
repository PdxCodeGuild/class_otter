"""
Lab 9: Compute Automated Readability Index
"""


import re
import math


def characters(words):
    count = len(re.findall(r"[a-zA-Z]", words))
    return count    

def sentences(text):    
    count = len(re.findall(r"[.!?]", text))  
    return count

def words(text):
    count = len(re.findall(r"[\w']+", text))
    return count


contents = ''
with open('text.txt', 'r') as f:
    contents = f.read()

ari = math.ceil(4.71 * ((characters(contents)) / (words(contents))) + 0.5 * ((words(contents)) / (sentences(contents))) - 21.43)

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

print()
print(f'The ARI score is: {ari}')
print(f"This corresponds to a {ari_scale[ari]['grade_level']}")
print(f"that is suitable for an average person {ari_scale[ari]['ages']} years old.")
print()