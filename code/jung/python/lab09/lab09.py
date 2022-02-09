import re
import math

with open('if_by_rudyard_kipling.txt') as f:
    contents = f.read()
    # print(contents)



# characters = #split by each letter (empty space?) 
char = re.split(r"[a-zA-Z0-9]", contents)
# print(char)

char_num = len(char)
# print(char_num)


# words = #split by " ", "\n", "-", 
words = re.split(r"[ \n—-]", contents)
# print(words)

words_num = len(words)
# print(words_num)


# sentence = #split by ".", "!", "?", ";", "'", ":"
sentence = re.split(r"[;:!]", contents)
# print(sentence)

sentence_num = len(sentence)
# print(sentence_num)


ari = 4.71 * (char_num/words_num) + 0.5 * (words_num/sentence_num) - 21.43
ari = math.ceil(ari)
# print(ari)

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


answer = ari_scale[ari]
# print(answer)

print(f"""The ARI for If_by_rudyard_kipling.txt is {ari}
This corresponds to a {ari_scale[ari]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari]['ages']} years old.""")
