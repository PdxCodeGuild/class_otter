text = 'text.txt'
f = open(text)  # open the file
contents = f.read()  # read the contents
# print()
# print(contents)
# print()
f.close()
periods = f"{contents}".count('.')
epoint = f"{contents}".count('!')
question = f"{contents}".count('?')
semi = f"{contents}".count(';')
#sentencecount
sentencecount = periods + epoint + question + semi
# print(sentencecount)
# print()
# print(len(contents))
whitecount = f"{contents}".count(' ')
# print()
# print(whitecount)
charactercount = len(contents) - whitecount
# print()
# print(charactercount)
#wordcount
words = (contents.split(' '))
# print()
# print(len(words))
# print()
wordcount = len(words)
# print(words)
#
#
#
sentencecount = float(sentencecount)
charactercount = float(charactercount)
wordcount = float(wordcount)
cw =(charactercount / wordcount)
ws = (wordcount / sentencecount)
comautoreadindex = (4.71 * cw) + (0.5 * ws) - 21.43
# print(comautoreadindex)
import math
c_a_r_i = math.ceil(comautoreadindex)
# print(c_a_r_i)
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
ari_age = ari_scale[c_a_r_i]['ages']
ari_grade = ari_scale[c_a_r_i]['grade_level']


print(f"The ARI for {text} is {c_a_r_i}\nThis corresponds to a {ari_grade} level of difficulty\nthat is suitable for an average person {ari_age} years old.")